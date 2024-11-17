import streamlit as st
import google.generativeai as genai
import re
from typing import Dict, Tuple

# Set your Gemini API key directly
GEMINI_API_KEY = "AIzaSyDum_fy1YX233Vi2mlp0VvbBz4YzMjXhlw"  # Add your API key here

class CodeReviewer:
    def __init__(self):
        """Initialize the CodeReviewer with Gemini AI."""
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')
        
    def review_code(self, code: str) -> Tuple[Dict, str]:
        """
        Review the provided code using Gemini AI.
        Returns a tuple of (issues_dict, fixed_code).
        """
        try:
            # Prompt engineering for better code review results
            prompt = f"""
            Please review the following Python code and provide:
            1. A list of potential bugs and issues
            2. Code quality improvements
            3. A corrected version of the code
            
            Here's the code to review:
            ```python
            {code}
            ```
            
            Please format your response exactly as shown below:
            ISSUES:
            - [issue description]
            
            IMPROVEMENTS:
            - [improvement suggestion]
            
            FIXED_CODE:
            ```python
            [corrected code]
            ```
            
            Please ensure to maintain this exact format in your response.
            """
            
            # Get response from Gemini
            response = self.model.generate_content(prompt)
            response_text = response.text
            
            # Initialize dictionary to store issues
            issues = {'bugs': [], 'improvements': []}
            
            # Extract issues
            issues_match = re.findall(r'ISSUES:\n(.*?)(?=IMPROVEMENTS:|FIXED_CODE:|$)', response_text, re.DOTALL)
            if issues_match:
                issues['bugs'] = [bug.strip() for bug in issues_match[0].split('\n') if bug.strip()]

            # Extract improvements
            improvements_match = re.findall(r'IMPROVEMENTS:\n(.*?)(?=FIXED_CODE:|$)', response_text, re.DOTALL)
            if improvements_match:
                issues['improvements'] = [imp.strip() for imp in improvements_match[0].split('\n') if imp.strip()]
            
            # Extract fixed code
            fixed_code_match = re.findall(r'```python\n(.*?)```', response_text, re.DOTALL)
            fixed_code = fixed_code_match[-1].strip() if fixed_code_match else ""
            
            return issues, fixed_code
        
        except Exception as e:
            st.error(f"Error during code review: {str(e)}")
            return {"bugs": [], "improvements": []}, ""


def main():
    st.set_page_config(
        page_title="AI Code Reviewer",
        page_icon="🔍",
        layout="wide"
    )
    
    st.title("🔍 AI Code Reviewer")
    st.subheader("Submit your Python code for an automated review")

    # Code input section - similar to Code 2 layout
    user_code = st.text_area("Paste your Python code below:", height=300)
    
    # Button to analyze code - after this, Gemini will review the code
    if st.button("Analyze Code"):
        if user_code.strip():
            with st.spinner("Analyzing your code..."):
                reviewer = CodeReviewer()
                issues, fixed_code = reviewer.review_code(user_code)
            
            # Display review results after analysis is done
            st.success("Analysis Complete!")

            # Show results
            st.subheader("💡 Suggested Improvements")
            for improvement in issues['improvements']:
                if improvement.strip():  # Skip empty lines
                    st.markdown(f"- {improvement.strip('- ')}")
            
            # Display fixed code
            st.subheader("Suggested Code")
            if fixed_code:
                st.code(fixed_code, language="python")
            
            # Display bugs
            st.subheader("Bugs")
            for bug in issues['bugs']:
                if bug.strip():  # Skip empty lines
                    st.markdown(f"- {bug.strip('- ')}")
        else:
            st.error("Please enter some Python code to analyze.")

if __name__ == "__main__":
    main()

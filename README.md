# AI Code Reviewer

An AI-powered Python code review tool built using **Streamlit** and **Google's Gemini AI** (or OpenAI's GPT, depending on your implementation). This application allows users to submit Python code, get feedback on potential bugs, improvements, and suggestions for code enhancements, as well as see a corrected version of the code.

## Features

- **Bug Detection**: The AI reviews the code and highlights potential bugs or errors.
- **Code Quality Suggestions**: Provides suggestions to improve the overall quality and readability of the code.
- **Code Correction**: Offers a fixed version of the code with improvements and bug fixes applied.
- **User-friendly Interface**: Built with Streamlit for easy and interactive code submission and review.

## Prerequisites

Before running the application, ensure that you have the following installed on your system:

- **Python** (version 3.7 or above)
- **Google Gemini API Key** or **OpenAI API Key** for code analysis

You can use `pip` to install the necessary libraries and dependencies.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/ai-code-reviewer.git
    cd ai-code-reviewer
    ```

2. **Create a virtual environment**:
    - On Windows:
      ```bash
      python -m venv venv
      ```
    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      ```

3. **Activate the virtual environment**:
    - On Windows:
      ```bash
      .\venv\Scripts\Activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies**:
    Install the required libraries and dependencies using `pip` from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

    If you don't have a `requirements.txt` file yet, you can generate it by running:
    ```bash
    pip freeze > requirements.txt
    ```

5. **Set up API keys**:
    - If using **Google Gemini AI**: 
      - Replace the placeholder `GEMINI_API_KEY = "KEY-KEY"` in the `CodeReviewer` class inside your Python code with your actual Gemini API key.
    - If using **OpenAI API**: 
      - Replace the OpenAI API key in the `analyze_code` function.

## Usage

1. **Run the Streamlit app**:
    Start the Streamlit server by running the following command:
    ```bash
    streamlit run app.py
    ```
    This will launch a local server and open the app in your browser.

2. **Submit your Python code**:
    Once the app is running, you can submit your Python code in the input box provided, and click the **Submit Code** button. The AI will analyze the code, detect potential bugs, and provide suggestions.

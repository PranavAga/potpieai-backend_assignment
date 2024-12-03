import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_anthropic import AnthropicLLM
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import json

load_dotenv(".env")
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

def analyze_pr_diff(code: bytes):
    """
    Analyze a GitHub PR diff for code style, bugs, performance, and best practices.

    Parameters:
    - code (str): The GitHub PR diff code

    Returns:
    - dict: Analysis results in the specified output format
    """
    # Define the prompt template for the analysis
    prompt = PromptTemplate.from_template(
        template=(
            "You are a code review assistant. Analyze the following code diff for the following aspects:\n"
            "1. Code style and formatting issues\n"
            "2. Potential bugs or errors\n"
            "3. Performance improvements\n"
            "4. Best practices\n\n"
            "Output your findings in JSON format with the structure:\n"
            "{{\"files\": [{{\"name\": <filename>, \"issues\": [{{\"type\": <style|bug|performance|best_practice>, \"line\": <line_number>, \"description\": <description>, \"suggestion\": <suggestion>}}]}}], \"summary\": {{\"total_files\": <int>, \"total_issues\": <int>, \"critical_issues\": <int>}}}}.\n"
            "Code diff:\n"
            "{code}"
        )
    )

    # Initialize the LLM
    llm = OpenAI(
        model="gpt-3.5-turbo-instruct",
        temperature=0,
        api_key=OPENAI_API_KEY
    )

    # Create a chain
    chain = prompt | llm

    analysis = chain.invoke(
        {
            "code": code
        }
    )

    # Parse and return the results
    return json.loads(analysis)
        
# Example usage
if __name__ == "__main__":
    code_diff = b"""diff --git a/main.py b/main.py
index 83db48f..bf9f3ad 100644
--- a/main.py
+++ b/main.py
@@ -13,6 +13,7 @@ def process_data(data):
     # Process the data
     result = None
     if data is not None:
+        print(data)
         result = data * 2
     return result

@@ -22,6 +23,7 @@ def main():
     data = None
     process_data(data)
"""

    result = analyze_pr_diff(code_diff)
    print(json.dumps(result, indent=4))

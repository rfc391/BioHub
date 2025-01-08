import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_test_cases(code_snippet):
    prompt = f"Write test cases for the following Python code:\n{code_snippet}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response['choices'][0]['text']

# Example usage
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "your_code.py")
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The required file '{file_path}' does not exist.")
with open(file_path, "r") as file:
    code = file.read()
print(generate_test_cases(code))

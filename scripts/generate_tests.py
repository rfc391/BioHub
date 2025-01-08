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
if not os.path.exists("your_code.py"):
    raise FileNotFoundError("The required file 'your_code.py' does not exist.")
with open("your_code.py", "r") as file:
    code = file.read()
print(generate_test_cases(code))

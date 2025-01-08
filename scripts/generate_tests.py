import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_test_cases(code_snippet):
    prompt = f"Write test cases for the following Python code:\n{code_snippet}"
response = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant for generating Python unit tests."},
        {"role": "user", "content": f"Generate test cases for the following code:\n{code}"}
    ]
)
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
response['choices'][0]['message']['content']
    # Example usage
with open("your_code.py", "r") as file:
    code = file.read()
print(generate_test_cases(code))

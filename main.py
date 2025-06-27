from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_completion(prompt, temperature=0.7, max_tokens=100, top_p=1.0):
    try:
        if not prompt.strip():
            return "Input cannot be empty. Please try again."

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p
            )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    print("Welcome to the Text Completion App (type 'exit' to quit)")
    while True:
        prompt = input("\nEnter your prompt: ")
        if prompt.lower() == "exit":
            break

        try:
            temp = float(input("Temperature (0-1, default 0.7): ") or 0.7)
            max_tokens = int(input("Max tokens (default 100): ") or 100)
            top_p = float(input("Top-p (0-1, default 1.0): ") or 1.0)
        except ValueError:
            print("Invalid parameter. Using default values.")
            temp, max_tokens, top_p = 0.7, 100, 1.0

        output = generate_completion(prompt, temperature=temp, max_tokens=max_tokens, top_p=top_p)
        print(f"\nAI-Powered Text Completion:\n\n{output}")

if __name__ == "__main__":
    main()

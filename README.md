# Capstone Project: AI-Powered Text Completion

A simple command-line application that uses OpenAI's GPT model to generate intelligent and creative text completions based on user prompts.

## Dependencies

This project requires:
- Python 3.7 or higher  
- [openai](https://pypi.org/project/openai/) ≥ 1.0.0  
- [python-dotenv](https://pypi.org/project/python-dotenv/)

To install all dependencies, run:

```bash
pip3 install openai python-dotenv
```

## API Key Setup

1. Sign up at OpenAI and generate an API key.
2. Create a file named `.env` in your project root.
3. Add the following line to it:

```env
OPENAI_API_KEY=your-openai-key-here
```

## Usage

To run the app:

```bash
python3 main.py
```

How it works:
- You'll be prompted to enter a custom prompt.
- You can then configure:
  - **Temperature (0–1)**: Controls creativity/randomness.
  - **Max Tokens**: Sets the maximum response length.
  - **Top-p (0–1)**: Controls diversity.
- The AI will return a response.
- Type `exit` to quit at any time.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

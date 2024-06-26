# -*- coding: utf-8 -*-
"""NM project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DiPau4-smtciXMbFMVro7jNDxKiaSaVE
"""

pip install openai
import openai
openai.api_key = 'your_openai_api_key'
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()
def main():
    print("AI Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("AI Chatbot: Goodbye! Have a great day!")
            break
        prompt = f"You: {user_input}\nAI Chatbot:"
        response = chat_with_gpt(prompt)
        print(response)
if __name__ == "__main__":
    main()
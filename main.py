import openai

import os   #THhis enables us to interact with our environmental variables hence we can access the API key
from dotenv  import load_dotenv         

load_dotenv()

open_ai_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    print("API key is missing or incorrect.")
    exit()

def get_completion (prompt, model="gpt-3.5-turbo"):
    try:
        response = openai.ChatCompletion.create(model = model,
        messages =[{
            'role': 'user', "content": prompt}
        ],
        temperature = 0)
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    prompt = input("How can i help you dear user?")
    ai_response = get_completion(prompt)
    print("Your Answer is: ", ai_response)
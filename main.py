import openai
import os   #THhis enables us to interact with our environmental variables hence we can access the API key
import dotenv  #This is a library that allows us to load our environmental variables from a .env file
import load_dotenv         # Does the same thing as the above line

load_dotenv()

open_ai_key = os.getenv("OPENAI_API_KEY")

def get_completion (prompt, model="gpt-3.5-turbo"):
    try:
        response = openai.ChatCompletion.create(
            model = model,
            messages =[{
                'role': 'user', "content": prompt}
            ],
            temperature = 0
            )
        return response.choices[0].message['content']
    except Exception as e:
        return f"An error occurred: {e}"
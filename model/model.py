import sys
from dotenv import load_dotenv
import os
from chatbot import ChatBot
import pandas as pd

def input_data():
    #os.chdir('..')
    os.chdir('data')

    data = pd.read_csv('monthly_data.csv')
    df_string = data.to_string(index=False)

    return df_string

def main():
    # Load environment variables from .env file
    load_dotenv()

    data_input = input_data()

    # Access the API key from the environment variable
    api_key = os.getenv("API_KEY")

    chatbot = ChatBot(api_key= api_key)
    chatbot.start_conversation()

    print("Welcome to the BudgetBud, your personalized financial advisor. Type 'quit' to exit.")


    
    while True:
        #choices = ['In which category can I reduce my expenses as my monthly salary is?', 'How do i save more according to my data?']
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            #print("Exiting Chabot")
            sys.exit('Exiting the ChatBot')

        try:
            response = chatbot.send_prompt(user_input + data_input)
            print(f"{chatbot.CHATBOT_NAME}: {response}")
        except Exception as e:
            print(f"Error: {e}")

main()
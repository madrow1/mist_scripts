#https://api.eu.mist.com/api/v1/labs/orgs/e6a9f8e5-71d4-45b2-8c2c-6c508f6fad4a/chatbot_converse
import requests
import api
import json

def main():
    marvis_chat = api.chat('api.json', "Hello, Marvis")
        
    response = requests.post(marvis_chat[0], headers=marvis_chat[1])
    print(response.text)

if __name__ == '__main__':
    main()
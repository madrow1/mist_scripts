import requests
import api
import json

def main():
    marvis_chat = api.chat('api.json', "Hello, Marvis")
        
    response = requests.post(marvis_chat[0], headers=marvis_chat[1])
    print(response.text)

if __name__ == '__main__':
    main()
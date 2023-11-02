import api
import requests

def main():
    api_response = api.get_api('api.json')
    print(requests.get(api_response[0], headers=api_response[1]))
    
if __name__ =='__main__':
    main()
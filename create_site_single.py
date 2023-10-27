import json
import time
import argparse
import requests
import api

def check_site_exists(configs):
    site_name = configs['site']['name']

    existing_site_details = api.get_api('api.json')
    response = requests.get(existing_site_details[0], headers=existing_site_details[1])

    for i in range(len(response.json())):
        if site_name in response.json()[i]['name']:
            return True
        else:
            return False 


def create_new_site(configs):
    apos_site = {}
    apos_site['name'] = configs['site']['name']
    apos_site['timezone'] = configs['site']['timezone']
    apos_site['country_code'] = configs['site']['country_code']
    apos_site['latlng'] = {'lat': configs['site']['lat'], 'lng': configs['site']['lng']}
    apos_site['address'] = configs['site']['address']

    data_post = json.dumps(apos_site)
    api_response = api.get_api('api.json')
    

    response = requests.post(api_response[0], data=data_post, headers=api_response[1])
    new_site = json.loads(response.content.decode('utf-8'))

    

def main():
    parser = argparse.ArgumentParser(description='Creates a new Mist site')
    parser.add_argument('config', metavar='config_file', type=argparse.FileType('r'), help='')
    args = parser.parse_args()
    configs = json.load(args.config)

    if check_site_exists(configs) == False:
        new_site_id = create_new_site(configs)
        print("New site {} created".format(configs['site']['name']))
    else:
        print("This site already exists")

if __name__ == "__main__":
    main()
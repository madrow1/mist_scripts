import json
import argparse
import requests

def get_api(file):
    f = open(file)
    configs = json.load(f)
    api_url = '{0}orgs/{1}/sites'.format(configs['api']['mist_url'],configs['api']['org_id'])
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Token {}'.format(configs['api']['token'])}
    return api_url,headers

def check_site_exists(configs):
    site_name = configs['site']['name']

    existing_site_details = get_api('api.json')
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
    api_response = get_api('api.json')
    

    response = requests.post(api_response[0], data=data_post, headers=api_response[1])
    new_site = json.loads(response.content.decode('utf-8'))


if __name__ == "__main__":
    get_api()


import json
import argparse
import requests

def read_json_site_list(file):
    f = open(file)
    json_file = json.load(f)
    return json_file

def get_api(file):
    f = open(file)
    configs = json.load(f)
    api_url = '{0}orgs/{1}/sites'.format(configs['api']['mist_url'],configs['api']['org_id'])
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Token {}'.format(configs['api']['token'])}
    return api_url,headers


def chat(file,post_request):
    f = open(file)
    configs = json.load(f)
    api_url = '{0}labs/orgs/{1}/chatbot_converse'.format(configs['api']['mist_url'],configs['api']['org_id'])
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Token {}'.format(configs['api']['token']),
               'data': post_request}
    return api_url,headers

def check_site_exists(configs):
    site_name = configs['site']['name']

    site_names = []

    existing_site_details = get_api('api.json')
    response = requests.get(existing_site_details[0], headers=existing_site_details[1])

    if len(site_names) != 0:
        if site_name in site_names:
            return True        
    else: 
        for i in range(len(response.json())):
            site_names.append(response.json()[i]['name'])

    if site_name in site_names:
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

def create_new_multi_site(configs):
    apos_site = {}
    apos_site['name'] = configs['name']
    apos_site['timezone'] = configs['timezone']
    apos_site['country_code'] = configs['country_code']
    apos_site['latlng'] = {'lat': configs['lat'], 'lng': configs['lng']}
    apos_site['address'] = configs['address']

    data_post = json.dumps(apos_site)
    api_response = get_api('api.json')
    
    response = requests.post(api_response[0], data=data_post, headers=api_response[1])
    new_site = json.loads(response.content.decode('utf-8'))

    if response.status_code == "200":
        print("Site {} created sucessfully".format(apos_site['name']))
    else:
        print("Site {} creation failed".format(apos_site['name']))


if __name__ == "__main__":
    get_api()


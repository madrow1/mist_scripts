import json
import time
import argparse
import requests


def create_new_site(configs):
    apos_site = {}
    apos_site['name'] = configs['site']['name']
    apos_site['timezone'] = configs['site']['timezone']
    apos_site['country_code'] = configs['site']['country_code']
    apos_site['latlng'] = {'lat': configs['site']['lat'], 'lng': configs['site']['lng']}
    apos_site['address'] = configs['site']['address']

    data_post = json.dumps(apos_site)
    api_url = '{0}orgs/{1}/sites'.format(configs['api']['mist_url'],configs['api']['org_id'])
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Token {}'.format(configs['api']['token'])}
    
    response = requests.post(api_url, data=data_post, headers=headers)
    new_site = json.loads(response.content.decode('utf-8'))

    if response.status_code == 200:
        print("{0} site has been created".format(configs['site']['name']))
    else:
        print("Something went wront: {}".format(response.status_code))

    

def main():
    parser = argparse.ArgumentParser(description='Creates a new Mist site')
    parser.add_argument('config', metavar='config_file', type=argparse.FileType('r'), help='')
    args = parser.parse_args()
    configs = json.load(args.config)

    new_site_id = create_new_site(configs)

if __name__ == "__main__":
    main()
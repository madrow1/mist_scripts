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

if __name__ == "__main__":
    get_api()
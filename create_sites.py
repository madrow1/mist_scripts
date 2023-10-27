import api 
import requests
import json 
import argparse

def read_json_site_list(file):
    f = open(file)
    sites = json.load(f)
    return sites

def main():
    sites = read_json_site_list('config.json')
    for i in range(len(sites)):
        if i == 0:
            print(sites['site'])
        else:
            print(sites['site{}'.format(i)])


#    if api.check_site_exists(configs) == False:
#        new_site_id = api.create_new_site(configs)
#        print("New site {} created".format(configs['site']['name']))
#    else:
#        print("This site already exists")
#    return quit


if __name__ == "__main__":
    main()
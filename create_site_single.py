import json
import time
import argparse
import requests
import api
    
def main():
    parser = argparse.ArgumentParser(description='Creates a new Mist site')
    parser.add_argument('config', metavar='config_file', type=argparse.FileType('r'), help='')
    args = parser.parse_args()
    configs = json.load(args.config)

    if api.check_site_exists(configs) == False:
        new_site_id = api.create_new_site(configs)
        print("New site {} created".format(configs['site']['name']))
    else:
        print("This site already exists")

if __name__ == "__main__":
    main()
import api 
import requests
import json 
import argparse

def main():
    parser = argparse.ArgumentParser(description='Creates a new Mist site')
    parser.add_argument('config', metavar='config_file', type=argparse.FileType('r'), help='')
    args = parser.parse_args()
    configs = json.load(args.config)

    print(configs)

    if api.check_site_exists(configs) == False:
        new_site_id = api.create_new_site(configs)
        print("New site {} created".format(configs['site']['name']))
    else:
        print("This site already exists")
    return quit


if __name__ == "__main__":
    main()
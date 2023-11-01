import api 
import requests
import json 
import argparse
import time

def main():
    sites = api.read_json_site_list('config.json')
    for i in range(len(sites)):
        if i == 0:
            start_time = time.time()
            api.create_new_multi_site(sites['site'])
            print("--- %s seconds ---" % (time.time() - start_time))
        else:
            start_time = time.time()
            api.create_new_multi_site(sites['site{}'.format(i)])
            print("--- %s seconds ---" % (time.time() - start_time))
   

if __name__ == "__main__":
    main()
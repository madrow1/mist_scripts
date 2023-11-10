import api 
import requests
import json 
import argparse
import time

def main():
    # Read in "config.json" This could be replaced with a variable 
    sites = api.read_json_site_list('config.json')
    for i in range(len(sites)):
        # If rannge len == 0 then the site should be just the site
        if i == 0:
            start_time = time.time()
            api.create_new_multi_site(sites['site'])
            print("--- %s seconds ---" % (time.time() - start_time))
        else: # If site =>1 then site{}.format means that "i" will be concatonated on the end. 
            start_time = time.time()
            api.create_new_multi_site(sites['site{}'.format(i)])
            print("--- %s seconds ---" % (time.time() - start_time))
   

if __name__ == "__main__":
    main()
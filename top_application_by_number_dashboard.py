# /api/v1/sites/3d59c02c-b7a6-4485-9f3a-f57d2a8e35fe/insights/site/3d59c02c-b7a6-4485-9f3a-f57d2a8e35fe/stats?end=1698400618&interval=600&start=1698361200&metrics=top-wlan-by-num_client,top-wlan-by-bytes,top-app-by-num_client,top-app-by-bytes
import api
import json
import time
import argparse
import requests
import panel as pn
import hvplot.pandas

print(api.get_api('api.json'))

api_response = api.get_api('api.json')

print(requests.get(api_response[0], headers=api_response[1]))
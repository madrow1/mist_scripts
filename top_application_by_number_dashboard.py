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
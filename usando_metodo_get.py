import requests

URL_BASE = 'http://127.0.0.1:5000'

endpoint = 'healthcheck'
response = requests.get(url=f'{URL_BASE}/{endpoint}')
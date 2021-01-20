import requests

URL_BASE = 'http://127.0.0.1:5000'

def get_healthcheck():
    endpoint = 'healthcheck'
    response = requests.get(url=f'{URL_BASE}/{endpoint}')
    status_code = response.status_code
    if status_code == 200:
        content = response.json()
        print(content['message'])

def get_technologies():
    endpoint = 'technologies'
    response = requests.get(url=f'{URL_BASE}/{endpoint}')
    status_code = response.status_code
    if status_code == 200:
        content = response.json()
        print(content['technologies'])
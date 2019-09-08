import json
import requests
import urllib

from ratelimit import limits, sleep_and_retry

with open("credentials.json") as f:
    API_KEY = json.load(f)['api_key']

url_base = "https://www.behindthename.com/api/"

name_look_up_url = url_base + "lookup.json"
related_names_url = url_base + "related.json"
random_names_url = url_base + "random.json"

@sleep_and_retry
@limits(calls=1, period=10)
def call_api(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f'API response: {format(response.status_code)}')
    return response


def get_random():
    response = call_api(f'{random_names_url}?key={API_KEY}')
    return response.json()

def get_related_names(name):
    response = call_api(f'{related_names_url}?key={API_KEY}&name={name}')
    return response.json()

def dump_related_names(names, outfile):
    with open(outfile, 'w') as f:
        pass
    
    for name in names:
        response = get_related_names(name)
        response['name'] = name
        with open(outfile, 'a') as f:
            json.dump(response, f)

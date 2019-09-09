import json
import requests
import urllib

from bs4 import BeautifulSoup
from ratelimit import limits, sleep_and_retry


with open("credentials.json") as f:
    API_KEY = json.load(f)['api_key']

base_url = "https://www.behindthename.com"

api_base_url = f"{base_url}/api"

meaning_base_url = f"{base_url}/name"

name_look_up_url = f"{api_base_url}/lookup.json"
related_names_url = f"{api_base_url}/related.json"
random_names_url = f"{api_base_url}/random.json"


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


def name_url(name):
    return f"{meaning_base_url}/{name.lower().strip()}"


def related_name_url(name):
    return f"{meaning_base_url}/{name.lower().strip()}/related"


@sleep_and_retry
@limits(calls=1, period=10)
def related_name_soup(name):
    url = related_name_url(name.lower().strip())
    response = requests.get(url)

    if response.status_code == 404:
        return None
    
    return BeautifulSoup(requests.get(url).content, 'html.parser')


def related_divs(soup):
    return soup.find_all("div", attrs={"class": "related-section"})


def parse_related_divs(related_results_set):
    names = [[r.get_text() for r in rel.find_all("a")] for rel in related_results_set]
    usage = [b.find("b").get_text() for b in related_results_set]

    return {u: n for (u, n) in zip(usage, names)}


def related_names(name):
    soup = related_name_soup(name)
    
    if not soup: 
        return None

    divs = related_divs(soup)
    if not divs:
        try:
            soup = related_name_soup(f"{name}-1")
            divs = related_divs(soup)
        except AttributeError:
            pass
    
    return parse_related_divs(divs)


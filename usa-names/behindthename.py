import json
import requests
import urllib
from collections import defaultdict

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
    response = requests_get(url)

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


@sleep_and_retry
@limits(calls=1, period=3)
def requests_get(url):
    return requests.get(url)


class BehindTheName:

    def __init__(self, name):
        self.name = name
        self.set_name_url()


    def set_name_url(self, get_soup=False):
        """If there are more than one, only get the top name."""
        self.url = name_url(f"{self.name}-1")
        response = requests_get(self.url)

        if response.status_code == 404:
            self.url = name_url(self.name)
            response = requests_get(self.url)
        
        if response.status_code == 404:
            self.exists = False
            return None
        else:
            self.exists = True

        if get_soup:
            return BeautifulSoup(response.content, 'html.parser')
        

    def related_name_url(self):
        return f"{self.url}/related"


    def related_name_soup(self):
        response = requests_get(self.related_name_url())
        return BeautifulSoup(response.content, 'html.parser')


    def related_divs(self, soup):
        return soup.find_all("div", attrs={"class": "related-section"})


    def parse_related_divs(self, related_results_set):
        names = [[r.get_text() for r in rel.find_all("a")] for rel in related_results_set]
        usage = [b.find("b").get_text() for b in related_results_set]

        rel_names = defaultdict(list)
        for u, n in zip(usage, names):
            rel_names[u] += n

        return rel_names


    def related_names(self):
        soup = self.related_name_soup()
        divs = self.related_divs(soup)
        return self.parse_related_divs(divs)


"""
names to test:
    David - single
    Dewi - multiple
    Daenerys - fictional
    Zuggit - nonexistent
"""
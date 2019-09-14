from behindthename import BehindTheName
import logging
import json

logging.basicConfig(filename='logs/download.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(message)s')

def get_unique_names():
    with open("data/unique_usa_names.csv") as fp:
        return [line.lower().strip() for line in fp.readlines()]

if (__name__ == "__main__"):
    # print("joe")
    names = get_unique_names()

    with open("data/related_names.json", "a") as fp:
        for name in names:
            related_names = BehindTheName(name).related_names()
            json.dump(obj={name: related_names}, fp=fp)
            logging.info(name)

#%%
from pathlib import Path
import json
from typing import NamedTuple
import pandas as pd

data_dir = Path("/home/david/Dropbox/Projects/100daysofweb-with-python-course/projects/usa-names/data")
usa_first_name_file = data_dir / 'usa_names.json'
test_file = data_dir / 'usa_names_test.json'
usa_last_name_file = data_dir / 'surnames_2010_census.csv'

#%%
class FirstNameRecord(NamedTuple):
    state: str
    gender: str
    year: int
    name: str
    number: int

#%%
def load_names_to_tuple(name_file):
    pass

def load_names_to_dataframe(name_file):
    df = pd.read_json(name_file)
    df["state"] = df["state"].astype("category")
    df["gender"] = df["gender"].astype("category")
    df["year"] = df["year"].astype(int)
    df["name"] = df["name"].astype(str)
    df["number"] = df["number"].astype(int)
    return df

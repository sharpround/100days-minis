from behindthename import dump_related_names

def get_unique_names():
    with open("data/unique_usa_names.csv") as fp:
        return [line.lower().strip() for line in fp.readlines()]

if (__name__ == "__main__"):
    # print("joe")
    names = get_unique_names()
    dump_related_names(names, "data/name_synonyms.json")
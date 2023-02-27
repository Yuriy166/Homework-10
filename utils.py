import json
from candidate import Candidate


def load_candidates(filename):
    with open(filename, encoding='utf-8') as f:
        return json.load(f)


def get_all(data):
    arr = []
    for item in data:
        candidate = Candidate(item['pk'], item['name'], item['position'], item['skills'].lower(), item['picture'])
        arr.append(candidate)
    return arr

def get_by_pk(pk, data):
    for item in data:
        if item.pk == pk:
            return pk

def get_by_skill(skill_name, data):
    arr = []
    for item in data:
        if skill_name in item.skills:
            arr.append(item)
    return arr

print(load_candidates(get_all('arr')))
import json

def lookup_cve(service):
    with open("data/cve_db.json") as f:
        db = json.load(f)
    return db.get(service, [])

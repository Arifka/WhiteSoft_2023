import json

def write_data2json(data: list):
    with open ("result.json", "w") as write:
        json.dump(data, write, indent=1)
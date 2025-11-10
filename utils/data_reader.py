import json

def get_json_data(filepath: str) -> list:
    with open(filepath, "r") as file:
        return json.load(file)
import requests
import json

def get_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    else:
        try:
            data = response.json()
        except json.JSONDecodeError as ex:
            raise SystemExit(ex)
        else:
            return data
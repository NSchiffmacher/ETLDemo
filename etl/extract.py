import requests
import os
from typing import Any

if 'JCDECAUX_API_KEY' not in os.environ:
    raise Exception("Please set the JCDECAUX_API_KEY environment variable")

JCDECAUX_API_TOKEN = os.environ['JCDECAUX_API_KEY']
CONTRACT_NAME = "toulouse" # Name of the VélÔToulouses contract in JCDecaux API


def get_stations_informations() -> list[dict[str, Any]]:
    url = f'https://api.jcdecaux.com/vls/v1/stations?contract={CONTRACT_NAME}&apiKey={JCDECAUX_API_TOKEN}'
    response = requests.get(url)
    return response.json()

import requests
from pprint import pprint

API_BASE_URL = "https://restcountries.com/"


response = requests.get(f"{API_BASE_URL}/v3.1/all?fields=name,flags")
json_data = response.json()

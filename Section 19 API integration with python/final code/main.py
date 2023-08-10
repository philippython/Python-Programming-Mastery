import os
from dotenv import load_dotenv
from datetime import datetime
import requests 
import pprint 
import json

load_dotenv()

API_KEY = os.environ.get("API_KEY")
# API_BASE_URL = "https://restcountries.com/"
API_BASE_URL = "https://holidayapi.com/"

paramaters = {
    "country" : "NGA",
    "key" : API_KEY,
    "year" : datetime.now().year - 1,
    "public" : True
}
# response = requests.get(f"{API_BASE_URL}/v3.1/all?fields=name,flags")
# json_data = response.json()
# pprint.pprint(json_data)

try: 
    response = requests.get(f"{API_BASE_URL}v1/holidays", params=paramaters)
    response.raise_for_status()
except Exception:
    if response.status_code >= 400:
        print("Client error occured!")
    elif response.status_code >= 500:
        print("Server error please try again later!")
else:
    with open(r"C:\Users\23490\Documents\Python Programming Mastery\Section 19 API integration with python\final code\response.json", "w") as response_data:
        json.dump(response.json(), response_data, indent=4)

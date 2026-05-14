import requests
import json
from pathlib import Path

MANAGER_ID = "33365"

RAW_PATH = Path("data/raw/history.json")


def fetch_history():
    url = f"https://fantasy.premierleague.com/api/entry/{MANAGER_ID}/history/"

    # Make a GET request to the API endpoint
    response = requests.get(url) 


    # Check if the request was successful and parse the JSON response to the data variable, otherwise print an error message and set data to an empty dictionary
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error fetching history data for manager {MANAGER_ID}")
        data = {}


    RAW_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Save the data to a JSON file named "history.json" with an indentation of 4 spaces for better readability
    with open(RAW_PATH, "w") as f:
        json.dump(data, f, indent=4)

    print("History data has been saved successfully")
import json
from pathlib import Path

import requests

RAW_PATH = Path("data/raw/bootstrap_static.json")

def fetch_bootstrap():
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        RAW_PATH.parent.mkdir(parents=True, exist_ok=True)

        with open(RAW_PATH, "w") as f:
            json.dump(data, f, indent=4)

        print("Bootstrap data has been saved successfully")

    else:
        print(f"Failed to fetch bootstrap data. Status code: {response.status_code}")


import json
from pathlib import Path

import requests

MANAGER_ID = "33365"

RAW_DIR = Path("data/raw/picks")


def fetch_picks():
    
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    # Fetch picks data for all gameweeks
    for gw in range(1, 39):

        output_path = RAW_DIR / f"picks_gw{gw}.json"

        # Skip already downloaded files
        if output_path.exists():
            print(f"Gameweek {gw} already exists. Skipping save.")
            continue


        url = (f"https://fantasy.premierleague.com/api/"
               f"entry/{MANAGER_ID}/event/{gw}/picks/")

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            with open(output_path, "w") as f:
                json.dump(data,f, indent=4)

            print(f"Saved picks for Gameweek {gw}")

        else:
            print(f"Failed to fetch picks for Gameweek {gw} "
                  f"Status code: {response.status_code}"
            )
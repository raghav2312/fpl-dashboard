import json
from pathlib import Path

import requests

RAW_DIR = Path("data/raw/live_points")


def fetch_live_points():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    # Fetch live points data for all gameweeks
    for gw in range(1, 39):

        output_path = RAW_DIR / f"live_points_gw{gw}.json"

        # Skip already downloaded files
        if output_path.exists():
            print(f"Gameweek {gw} already exists. Skipping save.")
            continue

        url = f"https://fantasy.premierleague.com/api/event/{gw}/live/"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            with open(output_path, "w") as f:
                json.dump(data, f, indent=4)

            print(f"Saved live points for Gameweek {gw}")

        else:
            print(f"Failed to fetch live points for Gameweek {gw} "
                  f"Status code: {response.status_code}"
            )
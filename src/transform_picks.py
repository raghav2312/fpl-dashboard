import json
import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/picks")
PROCESSED_PATH = Path("data/processed/manager_picks.csv")


def transform_picks():
    rows = []

    pick_files = sorted(RAW_PATH.glob("picks_gw*.json"))

    for file_path in pick_files:
        gameweek = int(file_path.stem.replace("picks_gw", ""))

        with open(file_path, "r") as f:
            data = json.load(f)

        picks =  data.get("picks", [])

        for player in picks:
            multiplier = player["multiplier"]
            position = player["position"]

            rows.append(
                {
                    "gameweek": gameweek,
                    "element": player["element"],
                    "position": position,
                    "multiplier": multiplier,
                    "is_captain": player["is_captain"],
                    "is_vice_captain": player["is_vice_captain"],
                    "is_starting": position <= 11,
                    "is_bench": position > 11
                }
            )

    df = pd.DataFrame(rows)

    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)

    print(f"Saved processed picks data to {PROCESSED_PATH}")
import json
from pathlib import Path    

import pandas as pd

RAW_DIR = Path("data/raw/live_points")
PROCESSED_PATH = Path("data/processed/player_gw_points.csv")

def transform_live_points():
    rows = []

    live_files = sorted(RAW_DIR.glob("live_points_gw*.json"))

    for file_path in live_files:
        gameweek = int(file_path.stem.replace("live_points_gw", ""))

        with open(file_path, "r") as f:
            data = json.load(f)

        elements = data.get("elements", [])

        for player in elements:

            stats = player.get("stats", {})

            rows.append(
                {
                    "gameweek": gameweek,
                    "player_id": player["id"],
                    "minutes": stats.get("minutes", 0),
                    "goals_scored": stats.get("goals_scored", 0),
                    "assists": stats.get("assists", 0),
                    "clean_sheets": stats.get("clean_sheets", 0),
                    "goals_conceded": stats.get("goals_conceded", 0),
                    "own_goals": stats.get("own_goals", 0),
                    "penalties_saved": player["stats"]["penalties_saved"],
                }
            )

    df = pd.DataFrame(rows)

    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)

    print(f"Saved processed player gameweek points data to {PROCESSED_PATH}")
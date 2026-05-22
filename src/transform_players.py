import json
from pathlib import Path

import pandas as pd

RAW_PATH = Path("data/raw/bootstrap_static.json")
PROCESSED_PATH = Path("data/processed/players.csv")

def transform_players():

    with open(RAW_PATH, "r") as f:
        data = json.load(f)

    players = data["elements"]
    teams = data["teams"]
    positions = data["element_types"]

    #Team lookup
    team_lookup = {team["id"]: team["name"] for team in teams}

    #position lookup
    position_lookup = {position["id"]: position["singular_name_short"] for position in positions}

    rows = []

    for player in players:

        rows.append(
            {
                "player_id": player["id"],
                "first_name": player["first_name"],
                "second_name": player["second_name"],
                "web_name": player["web_name"],
                "team": team_lookup[player["team"]],
                "position": position_lookup[player["element_type"]],
                "now_cost": player["now_cost"],
                "total_points": player["total_points"],
                "minutes": player["minutes"],
                "goals_scored": player["goals_scored"],
                "assists": player["assists"],
                "clean_sheets": player["clean_sheets"],
                "selected_by_percent": player["selected_by_percent"]
            }
        )

    df = pd.DataFrame(rows)

    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)

    print(f"Saved processed players data to {PROCESSED_PATH}")
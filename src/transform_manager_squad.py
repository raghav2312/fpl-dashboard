from pathlib import Path

import pandas as pd

PICKS_PATH = Path("data/processed/manager_picks.csv")
PLAYERS_PATH = Path("data/processed/players.csv")
OUTPUT_PATH = Path("data/processed/manager_squad.csv")

def transform_manager_squad():
    picks_df = pd.read_csv(PICKS_PATH)
    players_df = pd.read_csv(PLAYERS_PATH)

    # Perform the transformation logic here
    # Example: Merge picks with players data
    squad_df = pd.merge(picks_df, players_df, on="player_id", how="left")

    squad_df = squad_df[
        [
            "gameweek",
            "player_id",
            "web_name",
            "team",
            "position_x",
            "position_y",
            "multiplier",
            "is_captain",
            "is_vice_captain",
            "is_starting",
            "is_bench",
            "now_cost",
            "total_points",
            "selected_by_percent"
        ]
    ]

    squad_df = squad_df.rename(
        columns={
            "position_x": "squad_position",
            "position_y": "player_position",
            "web_name": "player_name"
        }
    )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    squad_df.to_csv(OUTPUT_PATH, index=False)

    print(f"Saved processed manager squad data to {OUTPUT_PATH}")
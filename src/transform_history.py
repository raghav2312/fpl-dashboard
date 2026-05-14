import json
import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/history.json")
PROCESSED_PATH = Path("data/processed/manager_history.csv")

# Function to transform the raw history data into a processed format suitable for analysis and visualization
def transform_history():
    with open(RAW_PATH, "r") as f:
        data = json.load(f)

    # Extract the "current" key from the data, which contains the relevant information about the manager's history, and store it in a variable named current
    current = data["current"]

    df = pd.DataFrame(current)

    #Keep the useful columns for the dashboard
    df = df[
        [
            "event",
            "points",
            "total_points",
            "rank",
            "rank_sort",
            "overall_rank",
            "bank",
            "value",
            "event_transfers",
            "event_transfers_cost",
            "points_on_bench"
        ]
    ]

    #renaming columns for better readability
    df = df.rename(
        columns={
            "event": "gameweek",
            "points": "gw_points",
            "rank": "gw_rank",
            "rank_sort": "gw_rank_sort",
            "bank": "money_in_the_bank",
            "value": "team_value",
            "event_transfers": "transfers",
            "event_transfers_cost": "transfer_cost",
            "points_on_bench": "bench_points"
        }
    )


    #Calculate rank change
    df["previous_overall_rank"] = df["overall_rank"].shift(1)
    df["rank_change"] = df["previous_overall_rank"] - df["overall_rank"]
    df["rank_change"] = df["rank_change"].fillna(0).astype(int)


    #If both data and processed directories don't exist, create them & exist_ok=True allows the function to not raise an error if the directories already exist
    PROCESSED_PATH.parent.mkdir(parents=True, exist_ok=True)

    #Save the processed data to a CSV file named "manager_history.csv" in the "data/processed" directory, without including the index column in the output file
    df.to_csv(PROCESSED_PATH, index=False)

    print(f"saved processed history to {PROCESSED_PATH}")


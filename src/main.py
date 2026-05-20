from src.fetch_bootstrap import fetch_bootstrap
from src.fetch_history import fetch_history
from src.fetch_picks import fetch_picks

from src.transform_history import transform_history
from src.transform_picks import transform_picks
from src.transform_players import transform_players

if __name__ == "__main__":
    fetch_bootstrap()
    fetch_history()
    fetch_picks()

    transform_history()
    transform_picks()
    transform_players()
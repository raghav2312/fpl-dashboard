from src.fetch_bootstrap import fetch_bootstrap
from src.fetch_history import fetch_history
from src.fetch_picks import fetch_picks
from src.fetch_live_points import fetch_live_points

from src.transform_history import transform_history
from src.transform_picks import transform_picks
from src.transform_players import transform_players
from src.transform_manager_squad import transform_manager_squad

if __name__ == "__main__":
    fetch_bootstrap()
    fetch_history()
    fetch_picks()
    fetch_live_points() 

    transform_history()
    transform_picks()
    transform_players()
    transform_manager_squad()
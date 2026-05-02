import pandas as pd
from src.Analysis.pandas.GoatFinderTennis import find_the_goat_tennis

def test_find_the_goat_tennis_returns_player_with_most_wins():
    players_df = pd.DataFrame([
        {"player_id": 1, "name_first": "Roger", "name_last": "Federer"},
        {"player_id": 2, "name_first": "Rafael", "name_last": "Nadal"},
    ])
    matches_df = pd.DataFrame([
        {"winner_id": 1, "loser_id": 2},
        {"winner_id": 1, "loser_id": 2},
        {"winner_id": 2, "loser_id": 1},
    ])
    # Mock read_csv
    import unittest.mock as mock
    with mock.patch("pandas.read_csv", return_value=matches_df):
        goat = find_the_goat_tennis(players_df, "atp")
    assert goat.nom == "Roger Federer"
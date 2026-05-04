from src.Parsers.adapters.LoLMatchLoader import LoLMatchLoader
from src.Model.Match import Match
import unittest.mock as mock

def test_lol_match_loader_returns_list_of_matches():
    fake_csv = [
        {"gameid": "1", "date": "2024-01-01", "team_blue": "T1", "team_red": "G2", "kills_team_blue": "15", "kills_team_red": "10"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        matches = LoLMatchLoader().load_all_matches()
    assert len(matches) == 1
    assert isinstance(matches[0], Match)
    assert matches[0].team1 == "T1"
    assert matches[0].score1 == 15
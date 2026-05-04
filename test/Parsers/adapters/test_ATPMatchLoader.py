from src.Parsers.adapters.ATPMatchLoader import ATPMatchLoader
from src.Model.Match import Match
import unittest.mock as mock
import csv

def test_atp_match_loader_returns_list_of_matches():
    fake_csv = [
        {"match_num": "1", "tourney_date": "20240101", "winner_id": "105777", "loser_id": "208029"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        matches = ATPMatchLoader().load_all_matches()
    assert len(matches) == 1
    assert isinstance(matches[0], Match)
    assert matches[0].team1 == "105777"
    assert matches[0].team2 == "208029"
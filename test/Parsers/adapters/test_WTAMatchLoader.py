from src.Parsers.adapters.WTAMatchLoader import WTAMatchLoader
from src.Model.Match import Match
import unittest.mock as mock

def test_wta_match_loader_returns_list_of_matches():
    fake_csv = [
        {"match_num": "299", "tourney_date": "20240101", "winner_id": "216347", "loser_id": "201493"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        matches = WTAMatchLoader().load_all_matches()
    assert len(matches) == 1
    assert isinstance(matches[0], Match)
    assert matches[0].team1 == "216347"
    assert matches[0].score1 == 0
from src.Parsers.adapters.StarcraftMatchLoader import StarcraftMatchLoader
from src.Model.Match import Match
import unittest.mock as mock


def test_starcraft_match_loader_returns_list_of_matches():
    fake_csv = [
        {"date": "2016-02-17", "round": "RO32", "group": "A", "best_of": "3",
         "player_1": "Rogue", "player_2": "Journey", "score_player_1": "0", "score_player_2": "2"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        matches = StarcraftMatchLoader().load_all_matches()
    assert len(matches) == 1
    assert isinstance(matches[0], Match)
    assert matches[0].team1 == "Rogue"
    assert matches[0].team2 == "Journey"
    assert matches[0].score1 == 0
    assert matches[0].score2 == 2


def test_starcraft_match_loader_returns_empty_list():
    fake_csv = []
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        matches = StarcraftMatchLoader().load_all_matches()
    assert matches == []
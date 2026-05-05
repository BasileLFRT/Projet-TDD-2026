from src.Parsers.adapters.CS2MatchLoader import CS2MatchLoader
from src.Model.Match import Match
import unittest.mock as mock

def test_cs2_match_loader_returns_list_of_matches():
    fake_csv = [
        {"date": "2025-11-24", "stage": "1", "round": "1", "best_of": "1", "team_1": "B8", "team_2": "M80", "score_team_1": "0", "score_team_2": "1"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        matches = CS2MatchLoader().load_all_matches()
    assert len(matches) == 1
    assert isinstance(matches[0], Match)
    assert matches[0].team1 == "B8"
    assert matches[0].score2 == 1
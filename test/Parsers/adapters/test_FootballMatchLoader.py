from src.Parsers.adapters.FootballMatchLoader import FootballMatchLoader
from src.Model.Match import Match
import unittest.mock as mock

def test_football_match_loader_returns_list_of_matches():
    fake_csv = [
        {"match_api_id": "123", "date": "2015-09-12", "home_team_api_id": "9987", "away_team_api_id": "9993", "home_team_goal": "2", "away_team_goal": "1"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        matches = FootballMatchLoader().load_all_matches()
    assert len(matches) == 1
    assert isinstance(matches[0], Match)
    assert matches[0].team1 == "9987"
    assert matches[0].score1 == 2
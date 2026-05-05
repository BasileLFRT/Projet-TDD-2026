from src.Parsers.adapters.ChampionsLeagueMatchLoader import ChampionsLeagueMatchLoader
from src.Model.Match import Match
import unittest.mock as mock

def test_champions_league_match_loader_returns_list_of_matches():
    fake_csv = [
        {"date": "2021-09-14", "team_home": "Young Boys", "team_away": "Manchester United", "score_team_home": "2", "score_team_away": "1"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        matches = ChampionsLeagueMatchLoader().load_all_matches()
    assert len(matches) == 1
    assert isinstance(matches[0], Match)
    assert matches[0].team1 == "Young Boys"
    assert matches[0].score1 == 2
    
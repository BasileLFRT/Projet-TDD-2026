from src.Parsers.adapters.ChampionsLeagueTeamLoader import ChampionsLeagueTeamLoader
from src.Model.Team import Team
import unittest.mock as mock

def test_champions_league_team_loader_returns_list_of_teams():
    fake_csv = [
        {"full_name": "Real Madrid Football Club", "short_name": "Real Madrid"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        teams = ChampionsLeagueTeamLoader().load_all_teams()
    assert len(teams) == 1
    assert isinstance(teams[0], Team)
    assert teams[0].nom == "Real Madrid Football Club"
    assert teams[0].abreviation == "Real Madrid"
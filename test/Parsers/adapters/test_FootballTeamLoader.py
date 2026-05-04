from src.Parsers.adapters.FootballTeamLoader import FootballTeamLoader
from src.Model.Team import Team
import unittest.mock as mock

def test_football_team_loader_returns_list_of_teams():
    fake_csv = [
        {"team_api_id": "9987", "team_long_name": "KRC Genk", "team_short_name": "GEN"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        teams = FootballTeamLoader().load_all_teams()
    assert len(teams) == 1
    assert isinstance(teams[0], Team)
    assert teams[0].nom == "KRC Genk"
    assert teams[0].abreviation == "GEN"
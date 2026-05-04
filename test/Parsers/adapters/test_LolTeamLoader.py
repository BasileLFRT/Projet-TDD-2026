from src.Parsers.adapters.LoLTeamLoader import LoLTeamLoader
from src.Model.Team import Team
import unittest.mock as mock

def test_lol_team_loader_returns_list_of_teams():
    fake_csv = [
        {"team": "T1", "team_abbreviation": "T1"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=iter(fake_csv)):
        teams = LoLTeamLoader().load_all_teams()
    assert len(teams) == 1
    assert isinstance(teams[0], Team)
    assert teams[0].nom == "T1"
    assert teams[0].abreviation == "T1"
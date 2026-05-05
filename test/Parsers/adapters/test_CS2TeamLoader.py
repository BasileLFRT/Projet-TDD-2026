from src.Parsers.adapters.CS2TeamLoader import CS2TeamLoader
from src.Model.Team import Team
import unittest.mock as mock

def test_cs2_team_loader_returns_list_of_teams():
    fake_csv = [
        {"team": "FURIA", "team_abbreviation": "FURIA", "location": "Brazil", "region": "South America"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        teams = CS2TeamLoader().load_all_teams()
    assert len(teams) == 1
    assert isinstance(teams[0], Team)
    assert teams[0].nom == "FURIA"
    assert teams[0].abreviation == "FURIA"
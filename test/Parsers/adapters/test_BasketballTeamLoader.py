from src.Parsers.adapters.BasketballTeamLoader import BasketballTeamLoader
from src.Model.Team import Team
import unittest.mock as mock

def test_basketball_team_loader_returns_list_of_teams():
    fake_csv = [
        {"id": "1610612737", "full_name": "Atlanta Hawks", "abbreviation": "ATL"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        teams = BasketballTeamLoader().load_all_teams()
    assert len(teams) == 1
    assert isinstance(teams[0], Team)
    assert teams[0].nom == "Atlanta Hawks"
    assert teams[0].abreviation == "ATL"
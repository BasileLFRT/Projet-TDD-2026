from src.Parsers.adapters.VolleyballMenTeamLoader import VolleyballMenTeamLoader
from src.Model.Team import Team
import unittest.mock as mock

def test_volleyball_men_team_loader_returns_list_of_teams():
    fake_csv = [
        {"country_code_1": "USA", "country_code_2": "ARG", "set_country_1": "3", "set_country_2": "0"},
        {"country_code_1": "BRA", "country_code_2": "USA", "set_country_1": "2", "set_country_2": "3"},
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=iter(fake_csv)):
        teams = VolleyballMenTeamLoader().load_all_teams()
    assert len(teams) == 3
    assert all(isinstance(t, Team) for t in teams)
    assert any(t.nom == "USA" for t in teams)
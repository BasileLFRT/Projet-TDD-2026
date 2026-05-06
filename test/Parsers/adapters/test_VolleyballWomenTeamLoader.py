from src.Parsers.adapters.VolleyballWomenTeamLoader import VolleyballWomenTeamLoader
from src.Model.Team import Team
import unittest.mock as mock

def test_volleyball_women_team_loader_returns_list_of_teams():
    fake_csv = [
        {"country_1": "Brazil", "country_2": "Kenya", "set_country_1": "3", "set_country_2": "0"},
        {"country_1": "USA", "country_2": "Brazil", "set_country_1": "1", "set_country_2": "3"},
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=iter(fake_csv)):
        teams = VolleyballWomenTeamLoader().load_all_teams()
    assert len(teams) == 3
    assert all(isinstance(t, Team) for t in teams)
    assert any(t.nom == "Brazil" for t in teams)
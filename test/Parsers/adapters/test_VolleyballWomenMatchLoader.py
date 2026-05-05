from src.Parsers.adapters.VolleyballWomenMatchLoader import VolleyballWomenMatchLoader
from src.Model.Match import Match
import unittest.mock as mock

def test_volleyball_women_match_loader_returns_list_of_matches():
    fake_csv = [
        {"date": "2024-07-29", "country_1": "Brazil", "country_2": "Kenya", "set_country_1": "3", "set_country_2": "0"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        matches = VolleyballWomenMatchLoader().load_all_matches()
    assert len(matches) == 1
    assert isinstance(matches[0], Match)
    assert matches[0].team1 == "Brazil"
    assert matches[0].score1 == 3
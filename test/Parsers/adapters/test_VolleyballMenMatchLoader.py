from src.Parsers.adapters.VolleyballMenMatchLoader import VolleyballMenMatchLoader
from src.Model.Match import Match
import unittest.mock as mock

def test_volleyball_men_match_loader_returns_list_of_matches():
    fake_csv = [
        {"date": "2024-07-27", "country_code_1": "USA", "country_code_2": "ARG", "set_country_1": "3", "set_country_2": "0"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        matches = VolleyballMenMatchLoader().load_all_matches()
    assert len(matches) == 1
    assert isinstance(matches[0], Match)
    assert matches[0].team1 == "USA"
    assert matches[0].score1 == 3
from src.Parsers.adapters.VolleyballWomenPlayerLoader import VolleyballWomenPlayerLoader
from src.Model.Player import Player
import unittest.mock as mock

def test_volleyball_women_player_loader_returns_list_of_players():
    fake_csv = [
        {"name": "CAZAUTE Helena", "birth_date": "1997-12-17"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        players = VolleyballWomenPlayerLoader().load_all_players()
    assert len(players) == 1
    assert isinstance(players[0], Player)
    assert players[0].nom == "CAZAUTE Helena"
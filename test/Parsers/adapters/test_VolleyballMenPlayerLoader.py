from src.Parsers.adapters.VolleyballMenPlayerLoader import VolleyballMenPlayerLoader
from src.Model.Player import Player
import unittest.mock as mock

def test_volleyball_men_player_loader_returns_list_of_players():
    fake_csv = [
        {"name": "FROMM Christian", "birth_date": "1990-08-15"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        players = VolleyballMenPlayerLoader().load_all_players()
    assert len(players) == 1
    assert isinstance(players[0], Player)
    assert players[0].nom == "FROMM Christian"
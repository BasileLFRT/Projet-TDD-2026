from src.Parsers.adapters.LoLPlayerLoader import LoLPlayerLoader
from src.Model.Player import Player
import unittest.mock as mock

def test_lol_player_loader_returns_list_of_players():
    fake_csv = [
        {"name": "Faker", "birthdate": "1996-05-07"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        players = LoLPlayerLoader().load_all_players()
    assert len(players) == 1
    assert isinstance(players[0], Player)
    assert players[0].nom == "Faker"
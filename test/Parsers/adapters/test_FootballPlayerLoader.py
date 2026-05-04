from src.Parsers.adapters.FootballPlayerLoader import FootballPlayerLoader
from src.Model.Player import Player
import unittest.mock as mock

def test_football_player_loader_returns_list_of_players():
    fake_csv = [
        {"player_name": "Zinedine Zidane"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        players = FootballPlayerLoader().load_all_players()
    assert len(players) == 1
    assert isinstance(players[0], Player)
    assert players[0].nom == "Zinedine Zidane"
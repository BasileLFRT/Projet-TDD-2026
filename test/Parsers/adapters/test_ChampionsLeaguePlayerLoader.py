from src.Parsers.adapters.ChampionsLeaguePlayerLoader import ChampionsLeaguePlayerLoader
from src.Model.Player import Player
import unittest.mock as mock

def test_champions_league_player_loader_returns_list_of_players():
    fake_csv = [
        {"player_name": "Lionel Messi"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        players = ChampionsLeaguePlayerLoader().load_all_players()
    assert len(players) == 1
    assert isinstance(players[0], Player)
    assert players[0].nom == "Lionel Messi"
    assert players[0].player_api_id is None
from src.Parsers.adapters.ChessMatchLoader import ChessMatchLoader
from src.Model.Match import Match
import unittest.mock as mock

def test_chess_match_loader_returns_list_of_matches():
    fake_csv = [
        {"match": "1", "player_1": "Gukesh D", "player_2": "Carlsen", "score_player_1": "1", "score_player_2": "0", "round": "1", "section": "1", "seed_player_1": "1", "seed_player_2": "2"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        matches = ChessMatchLoader().load_all_matches()
    assert len(matches) == 1
    assert isinstance(matches[0], Match)
    assert matches[0].team1 == "Gukesh D"
    assert matches[0].score1 == 1.0
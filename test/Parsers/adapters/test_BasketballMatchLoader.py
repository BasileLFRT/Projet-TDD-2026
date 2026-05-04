from src.Parsers.adapters.BasketballMatchLoader import BasketballMatchLoader
from src.Model.Match import Match
import unittest.mock as mock

def test_basketball_match_loader_returns_list_of_matches():
    fake_csv = [
        {"game_id": "1", "game_date": "2024-01-01", "team_id_home": "1610612737", "team_id_away": "1610612738", "pts_home": "110", "pts_away": "105"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        matches = BasketballMatchLoader().load_all_matches()
    assert len(matches) == 1
    assert isinstance(matches[0], Match)
    assert matches[0].score1 == 110
    assert matches[0].score2 == 105
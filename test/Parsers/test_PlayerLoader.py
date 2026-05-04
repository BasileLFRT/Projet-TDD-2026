from src.Parsers.PlayerLoader import PlayerLoader
from src.Model.Sport import Sport
from src.Model.Competition import Competition
import unittest.mock as mock

def test_player_loader_raises_exception_for_unsupported_competition():
    loader = PlayerLoader()
    sport = Sport(nom="football")
    competition = Competition(id=99, nom="ligue_inconnue", sport="football", annee=2024)
    try:
        loader.load_all_players(sport, competition)
        assert False, "Aurait dû lever une exception"
    except Exception as e:
        assert str(e) == "Sport/Compétition non supporté"

def test_player_loader_uses_sport_nom_when_no_competition():
    loader = PlayerLoader()
    sport = Sport(nom="basketball")
    fake_players = [mock.MagicMock()]
    with mock.patch("src.Parsers.adapters.BasketballPlayerLoader.BasketballPlayerLoader.load_all_players", return_value=fake_players):
        result = loader.load_all_players(sport, None)
    assert result == fake_players
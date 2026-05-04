from src.Parsers.MatchLoader import MatchLoader
from src.Model.Sport import Sport
from src.Model.Competition import Competition
import unittest.mock as mock

def test_match_loader_raises_exception_for_unsupported_competition():
    loader = MatchLoader()
    sport = Sport(nom="football")
    competition = Competition(id=99, nom="ligue_inconnue", sport="football", annee=2024)
    try:
        loader.load_all_matches(sport, competition)
        assert False, "Aurait dû lever une exception"
    except Exception as e:
        assert str(e) == "Compétition non supportée"

def test_match_loader_uses_sport_nom_when_no_competition():
    loader = MatchLoader()
    sport = Sport(nom="basketball")
    fake_matches = [mock.MagicMock()]
    with mock.patch("src.Parsers.adapters.BasketballMatchLoader.BasketballMatchLoader.load_all_matches", return_value=fake_matches):
        result = loader.load_all_matches(sport, None)
    assert result == fake_matches
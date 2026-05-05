from src.Model.Sport import Sport
import pytest

def test_sport_constructor_is_ok_with_valid_sport():
    sport = Sport(nom="football")
    assert sport.nom == "football"
 
def test_sport_constructor_raises_value_error_with_invalid_sport():
    with pytest.raises(ValueError):
        Sport(nom="pingpong")
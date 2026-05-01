import pytest
from unittest.mock import patch, mock_open

from src.Parsers.adapters.LoLTeamLoader import LoLTeamLoader
from src.Parsers.TeamLoader import TeamLoader
from src.Model.Sport import Sport
from src.Model.Competition import Competition


LOL_CSV_CONTENT = """team,team_abbreviation,location,region
Team Heretics,TH,Spain,EMEA
Team Vitality,VIT,France,EMEA
Fnatic,FNC,United Kingdom,EMEA
"""


class TestLoLTeamLoader:
    @patch("builtins.open", mock_open(read_data=LOL_CSV_CONTENT))
    def test_load_returns_list(self):
        teams = LoLTeamLoader().load_all_teams()
        assert isinstance(teams, list)

    @patch("builtins.open", mock_open(read_data=LOL_CSV_CONTENT))
    def test_load_correct_count(self):
        teams = LoLTeamLoader().load_all_teams()
        assert len(teams) == 3

    @patch("builtins.open", mock_open(read_data=LOL_CSV_CONTENT))
    def test_team_nom(self):
        teams = LoLTeamLoader().load_all_teams()
        assert teams[0].nom == "Team Heretics"

    @patch("builtins.open", mock_open(read_data=LOL_CSV_CONTENT))
    def test_team_abreviation(self):
        teams = LoLTeamLoader().load_all_teams()
        assert teams[0].abreviation == "TH"

    @patch("builtins.open", mock_open(read_data=LOL_CSV_CONTENT))
    def test_team_ids_are_unique(self):
        teams = LoLTeamLoader().load_all_teams()
        ids = [t.id for t in teams]
        assert len(ids) == len(set(ids))

    @patch("builtins.open", mock_open(read_data=LOL_CSV_CONTENT))
    def test_empty_csv(self):
        with patch("builtins.open", mock_open(read_data="team,team_abbreviation,location,region\n")):
            teams = LoLTeamLoader().load_all_teams()
            assert teams == []


class TestTeamLoader:
    @patch("builtins.open", mock_open(read_data=LOL_CSV_CONTENT))
    def test_load_with_competition(self):
        competition = Competition(id=1, nom="lol", sport="lol", annee=2024)
        teams = TeamLoader().load_all_teams(sport=None, competition=competition)
        assert len(teams) == 3

    def test_unsupported_sport_raises(self):
        sport = Sport(nom="tennis")
        with pytest.raises(Exception, match="non supporté"):
            TeamLoader().load_all_teams(sport=sport)

    def test_unsupported_competition_raises(self):
        competition = Competition(id=99, nom="sport_inconnu", sport="inconnu", annee=2024)
        with pytest.raises(Exception, match="non supporté"):
            TeamLoader().load_all_teams(sport=None, competition=competition)

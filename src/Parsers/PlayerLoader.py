from typing import List

from src.Model.Player import Player
from src.Model.Competition import Competition
from .adapters.FootballPlayerLoader import FootballPlayerLoader
from .adapters.ChampionsLeaguePlayerLoader import ChampionsLeaguePlayerLoader

# Config only once per app
player_loaders_by_competition = {
    "european_leagues": FootballPlayerLoader,
    "champions_league": ChampionsLeaguePlayerLoader,
}



class PlayerLoader :
    def load_all_players(self, competition: Competition) -> List[Player]:
        loader = player_loaders_by_competition.get(competition.nom)

        if loader is None:
            raise Exception("Compétition non supporté")

        return loader().load_all_players()

from typing import List

from src.Model.Player import Player
from src.Model.Competition import Competition
from src.Model.Sport import Sport
from .adapters.FootballPlayerLoader import FootballPlayerLoader
from .adapters.ChampionsLeaguePlayerLoader import ChampionsLeaguePlayerLoader
from .adapters.BasketballPlayerLoader import BasketballPlayerLoader
from .adapters.ATPPlayerLoader import ATPPlayerLoader
from .adapters.WTAPlayerLoader import WTAPlayerLoader
from .adapters.VolleyballMenPlayerLoader import VolleyballMenPlayerLoader
from .adapters.VolleyballWomenPlayerLoader import VolleyballWomenPlayerLoader
from .adapters.ChessPlayerLoader import ChessPlayerLoader
from .adapters.BadmintonPlayerLoader import BadmintonPlayerLoader
from .adapters.LoLPlayerLoader import LoLPlayerLoader
from .adapters.CS2PlayerLoader import CS2PlayerLoader

# Config only once per app
player_loaders_by_competition = {
    "european_leagues": FootballPlayerLoader,
    "champions_league": ChampionsLeaguePlayerLoader,
    "basketball": BasketballPlayerLoader,
    "atp": ATPPlayerLoader,
    "wta": WTAPlayerLoader,
    "volleyball_men": VolleyballMenPlayerLoader,
    "volleyball_women": VolleyballWomenPlayerLoader,
    "chess": ChessPlayerLoader,
    "badminton": BadmintonPlayerLoader,
    "lol": LoLPlayerLoader,
    "cs2": CS2PlayerLoader
}



class PlayerLoader :
    def load_all_players(self, sport: Sport, competition: Competition = None) -> list[Player]:
        key = competition.nom if competition else sport.nom
        loader = player_loaders_by_competition.get(key)
        if loader is None:
            raise Exception("Sport/Compétition non supporté")
        return loader().load_all_players()

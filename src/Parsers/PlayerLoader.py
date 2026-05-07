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
from .adapters.StarcraftPlayerLoader import StarcraftPlayerLoader

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
    "league_of_legends": LoLPlayerLoader,
    "counter_strike_2": CS2PlayerLoader,
    "starcraft_2": StarcraftPlayerLoader
}


class PlayerLoader :
    """Permet de charger les données de joueurs à partir de fichiers csv
    
    C'est la classe centrale pour charger les données de joueurs,
    elle délègue le travail aux classes spécifiques à chaque sport ou compétition
    """
    def load_all_players(self, sport: Sport, competition: Competition = None) -> list[Player]:
        """Charge tous les joueurs d'un sport ou d'une compétition donnée
        
        Returns:
            list[Player]: La liste de tous les joueurs chargés
        
        Raises:
            Exception: Si le sport ou la compétition n'est pas supportée"""
        key = competition.nom if competition else sport.nom
        loader = player_loaders_by_competition.get(key)
        if loader is None:
            raise Exception("Sport/Compétition non supporté")
        return loader().load_all_players()

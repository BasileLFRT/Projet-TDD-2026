from src.Model.Match import Match
from src.Model.Competition import Competition
from src.Model.Sport import Sport
from .adapters.FootballMatchLoader import FootballMatchLoader
from .adapters.ChampionsLeagueMatchLoader import ChampionsLeagueMatchLoader
from .adapters.BasketballMatchLoader import BasketballMatchLoader
from .adapters.ATPMatchLoader import ATPMatchLoader
from .adapters.WTAMatchLoader import WTAMatchLoader
from .adapters.VolleyballMenMatchLoader import VolleyballMenMatchLoader
from .adapters.VolleyballWomenMatchLoader import VolleyballWomenMatchLoader
from .adapters.ChessMatchLoader import ChessMatchLoader
from .adapters.BadmintonMatchLoader import BadmintonMatchLoader
from .adapters.LoLMatchLoader import LoLMatchLoader
from .adapters.CS2MatchLoader import CS2MatchLoader
from .adapters.StarcraftMatchLoader import StarcraftMatchLoader

match_loaders_by_competition = {
    "european_leagues": FootballMatchLoader,
    "champions_league": ChampionsLeagueMatchLoader,
    "basketball": BasketballMatchLoader,
    "atp": ATPMatchLoader,
    "wta": WTAMatchLoader,
    "volleyball_men": VolleyballMenMatchLoader,
    "volleyball_women": VolleyballWomenMatchLoader,
    "chess": ChessMatchLoader,
    "badminton": BadmintonMatchLoader,
    "league_of_legends": LoLMatchLoader,
    "counter_strike_2": CS2MatchLoader,
    "starcraft_2": StarcraftMatchLoader,
}


class MatchLoader():
    """Permet de charger les données de matchs à partir de fichiers csv
    
    C'est la classe centrale pour charger les données de matchs,
    elle délègue le travail aux classes spécifiques à chaque sport ou compétition
    """
    def load_all_matches(self, sport: Sport, competition: Competition = None) -> list[Match]:
        """Charge tous les matchs d'un sport ou d'une compétition donnée
        
        Returns:
            list[Match]: La liste de tous les matchs chargés
            
        Raises:
            Exception: Si le sport ou la compétition n'est pas supportée
        """
        key = competition.nom if competition else sport.nom
        loader = match_loaders_by_competition.get(key)
        if loader is None:
            raise Exception("Compétition non supportée")
        return loader().load_all_matches()

        # if sport.name == "football":
        #     # Ce sont ces classes {Sport}MatchLoader qui "savent" où lire les données csv
        #     # et les convertir en objet Match
        #     return FootballMatchLoader().load_all_matches()
        # elif sport.name == "tennis":
        #     return TennisMatchLoader().load_all_matches()
        # else:
        #     raise Exception("Sport non supporté")


# Exemple d'utilisation
#mes_matchs: df[Match] = MatchLoader.load_all_matches(Sport(name="tourniquet artistique"))
from src.Model.Match import Match
from src.Model.Competition import Competition
from src.Model.Sport import Sport
from .adapters.FootballMatchLoader import FootballMatchLoader
from .adapters.ChampionsLeagueMatchLoader import ChampionsLeagueMatchLoader
from .adapters.BasketballMatchLoader import BasketballMatchLoader
from .adapters.ATPMatchLoader import ATPMatchLoader
from .adapters.WTAMatchLoader import WTAMatchLoader

match_loaders_by_competition = {
    "european_leagues": FootballMatchLoader,
    "champions_league": ChampionsLeagueMatchLoader,
    "basketball": BasketballMatchLoader,
    "atp": ATPMatchLoader,
    "wta": WTAMatchLoader,
}


class MatchLoader():
    def load_all_matches(self, sport: Sport, competition: Competition = None) -> list[Match]:
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
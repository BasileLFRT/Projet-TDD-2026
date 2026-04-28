from src.Model.Match import Match
from src.Model.Sport import Sport
from .adapters.FootballMatchLoader import FootballMatchLoader

match_loaders_by_sport = {
    "football": FootballMatchLoader,
}


class MatchLoader():
    def load_all_matches(self, sport: Sport) -> list[Match]:
        loader = match_loaders_by_sport.get(sport.nom)

        if loader is None:
            raise Exception("Sport non supporté")

        return loader.load_all_matches()

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
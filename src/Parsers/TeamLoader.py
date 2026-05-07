from src.Model.Team import Team
from src.Model.Competition import Competition
from src.Model.Sport import Sport
from .adapters.FootballTeamLoader import FootballTeamLoader
from .adapters.LoLTeamLoader import LoLTeamLoader
from .adapters.ChampionsLeagueTeamLoader import ChampionsLeagueTeamLoader
from .adapters.BasketballTeamLoader import BasketballTeamLoader
from .adapters.CS2TeamLoader import CS2TeamLoader
from .adapters.VolleyballMenTeamLoader import VolleyballMenTeamLoader
from .adapters.VolleyballWomenTeamLoader import VolleyballWomenTeamLoader

team_loaders_by_competition = {
    "european_leagues": FootballTeamLoader,
    "champions_league": ChampionsLeagueTeamLoader,
    "basketball": BasketballTeamLoader,
    "lol": LoLTeamLoader,
    "cs2": CS2TeamLoader,
    "volleyball_men": VolleyballMenTeamLoader,
    "volleyball_women": VolleyballWomenTeamLoader
}


class TeamLoader:
    """Permet de charger les données d'équipes à partir de fichiers csv
    
    C'est la classe centrale pour charger les données d'équipes,
    elle délègue le travail aux classes spécifiques à chaque sport ou compétition
    """
    def load_all_teams(self, sport: Sport, competition: Competition = None) -> list[Team]:
        """Charge tous les équipes d'un sport ou d'une compétition donnée

        Returns:
            list[Team]: La liste de tous les équipes chargés

        Raises:
            Exception: Si le sport ou la compétition n'est pas supportée ou si le sport est individuel (sans équipes)
            """
        key = competition.nom if competition else sport.nom
        loader = team_loaders_by_competition.get(key)
        if loader is None:
            raise Exception("Sport/Compétition non supporté ou sans équipes (sport individuel ?)")
        return loader().load_all_teams()
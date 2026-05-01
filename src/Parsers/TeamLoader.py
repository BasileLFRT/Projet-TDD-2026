from src.Model.Team import Team
from src.Model.Competition import Competition
from src.Model.Sport import Sport
from .adapters.FootballTeamLoader import FootballTeamLoader
from .adapters.LoLTeamLoader import LoLTeamLoader

team_loaders_by_competition = {
    "european_leagues": FootballTeamLoader,
    "lol": LoLTeamLoader,
    # "champions_league": ChampionsLeagueTeamLoader,  # à ajouter quand disponible
    # "basketball": BasketballTeamLoader,              # à ajouter quand disponible
}


class TeamLoader:
    def load_all_teams(self, sport: Sport, competition: Competition = None) -> list[Team]:
        key = competition.nom if competition else sport.nom
        loader = team_loaders_by_competition.get(key)
        if loader is None:
            raise Exception("Sport/Compétition non supporté ou sans équipes (sport individuel ?)")
        return loader().load_all_teams()
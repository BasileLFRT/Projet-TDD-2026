from typing import List

from src.Model.Player import Player
from src.Model.Sport import Sport
from .Adapters.FootballPlayerLoader import FootballPlayerLoader


# Config only once per app
player_loaders_by_sport = {
    "football": FootballPlayerLoader('./data/football/player.csv'),
}



class PlayerLoader :
    def load_all_players(self, sport: Sport) -> List[Player]:

        try:
            loader = player_loaders_by_sport[sport.name]
            return loader.load_all_players()
        except KeyError:
            raise TypeError("Sport non supporté")
from typing import List

from src.Model.Player import Player
from src.Model.Sport import Sport
from .adapters.FootballPlayerLoader import FootballPlayerLoader


# Config only once per app
player_loaders_by_sport = {
    "football": FootballPlayerLoader,
}



class PlayerLoader :
    def load_all_players(self, sport: Sport) -> List[Player]:
        loader = player_loaders_by_sport.get(sport.nom)

        if loader is None:
            raise Exception("Sport non supporté")

        return loader().load_all_players()

if __name__ == "__main__":
    players = PlayerLoader().load_all_players(Sport(nom="football"))
    for player in players:
        print(player)
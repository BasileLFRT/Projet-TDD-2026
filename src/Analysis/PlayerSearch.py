from typing import List

from src.Model.Player import Player

# Note for students :
# This class could be a static class, it does not explicitly need a constructor.
# It could also be simply a module that exports the methods and removes the class altogether because Python doesn't require everything to be an object!


class PlayerSearch:
    def filter_players_by_full_name(
        self, players: List[Player], search_string: str
    ) -> List[Player]:
        # This syntax is called "list comprehension" in Python, and can be handy for simple filtering like this :)
        return [player for player in players if player.nom == search_string]
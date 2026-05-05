import csv
from src.Model.Player import Player

class BasketballPlayerLoader:
    """Classe permettant de charger les données des joueurs de basketball à partir d'un fichier CSV.

    Lit les données du fichier 'player.csv' lié au basket et en crée des instances de Player
    """
    def load_all_players(self) -> list[Player]:
        """ Lit le fichier CSV de basketball et en liste les joueurs

        Returns:
            list[Player]: Une liste d'instances Player qui sont les joueurs chargés
        Raises:
            FileNotFoundError: Si le fichier CSV voulu n'est pas trouvé
        """
        players_list = []
        with open('./data/basketball/player.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player = Player(
                    nom=f"{row['first_name']} {row['last_name']}",
                    birthdate=None,
                    player_api_id=row.get("person_id")
                )
                players_list.append(player)
        return players_list

if __name__ == "__main__":
    players = BasketballPlayerLoader().load_all_players()
    for player in players:
        print(player)
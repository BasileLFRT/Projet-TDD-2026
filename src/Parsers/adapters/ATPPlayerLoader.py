import csv
from src.Model.Player import Player

class ATPPlayerLoader:
    """Classe permettant de charger les données des joueurs ATP à partir d'un fichier CSV.
    
    Lit les données du fichier 'atp_players_2024.csv' et en crée des instances de Player"""
    def load_all_players(self) -> list[Player]:
        """ Lit le fichier CSV ATP et en liste les joueurs
        
        Returns:
            list[Player]: Une liste d'instances Player qui sont les joueurs chargés
        
        Raises:
            FileNotFoundError: Si le fichier CSV voulu n'est pas trouvé"""
        players_list = []
        with open('./data/tennis/atp_players_2024.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player = Player(
                    nom=f"{row['name_first']} {row['name_last']}",
                    birthdate=None,
                    player_api_id=row.get("player_id")
                )
                players_list.append(player)
        return players_list

if __name__ == "__main__":
    players = ATPPlayerLoader().load_all_players()
    for player in players:
        print(player)
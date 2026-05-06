import csv
from src.Model.Player import Player

class WTAPlayerLoader:
    """Charge les joueuses WTA à partir d'un fichier CSV et les convertit en instances de Player.
    
    utilise les colonnes player_id, name_first, name_last du fichier wta_players_2024.csv 
    """
    def load_all_players(self) -> list[Player]:
        """Lit le fichier CSV et crée une liste d'instances de Player à partir des données.
        
        Returns:
            list[Player]: Une liste d'instances de Player représentant les joueuses
        
        Raises:
            FileNotFoundError: Si le fichier CSV n'est pas trouvé.
            KeyError: Si les colonnes attendues ne sont pas présentes dans le CSV. 
        """
        players_list = []
        with open('./data/tennis/wta_players_2024.csv', newline='') as csvfile:
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
    players = WTAPlayerLoader().load_all_players()
    for player in players:
        print(player)
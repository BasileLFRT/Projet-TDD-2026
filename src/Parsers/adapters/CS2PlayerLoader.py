import csv
from src.Model.Player import Player

class CS2PlayerLoader:
    """Classe qui charge les joueurs de CS à partir d'un fichier CSV et les instancie en Player.
    
    Le fichier CSV doit avoir les colonnes name, birthdate, pseudo.
    """
    def load_all_players(self) -> list[Player]:
        """Charge tous les joueurs de CS à partir du fichier CSV et les renvoie sous forme de liste de Player.
        
        Returns:
            list[Player]: La liste des joueurs chargés.
        Raises:
            FileNotFoundError: Si le fichier CSV n'est pas trouvé.
            KeyError: Si les colonnes attendues ne sont pas présentes dans le CSV."""
        players_list = []
        with open('./data/counter_strike_2/player.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                player = Player(
                    nom=row['name'],
                    birthdate=row.get('birthdate'),
                    player_api_id=row.get('pseudo')
                )
                players_list.append(player)
        return players_list

if __name__ == "__main__":
    players = CS2PlayerLoader().load_all_players()
    for player in players:
        print(player)
import csv
from src.Model.Player import Player

class ChessPlayerLoader:
    """Charge les joueurs d'échecs à partir d'un fichier CSV et les convertit en objets Player.
    
    Utilise les colonnes 'name', 'birth_year' et 'fide_id' du fichier CSV
    """
    def load_all_players(self) -> list[Player]:
        """Charge tous les joueurs d'échecs à partir du fichier CSV et les retourne sous forme de liste d'objets Player.
        
        Returns:
            list[Player]: Une liste d'objets Player représentant les joueurs d'échecs
        
        Raises:
            FileNotFoundError: Si le fichier CSV n'est pas trouvé
            KeyError: Si les colonnes attendues ne sont pas présentes dans le fichier CSV"""
        players_list = []
        with open('./data/chess/player.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                raw_name = row['name']
                if ',' in raw_name:
                    parts = raw_name.split(',', 1)
                    nom = f"{parts[1].strip()} {parts[0].strip()}"
                else:
                    nom = raw_name
                player = Player(
                    nom=nom,
                    birthdate=row.get('birth_year'),
                    player_api_id=row.get('fide_id')
                )
                players_list.append(player)
        return players_list
import csv
from src.Model.Player import Player

class ChampionsLeaguePlayerLoader:
    """Classe permettant de charger des joueurs de la Ligue des Champions depuis un fichier CSV.
    
    Lit les données du fichier player.csv lié au football et en crée des instances de Player
    avec les colonnes : player_name. Les champs birthdate et player_api_id sont None au départ
    et doivent être assignés manuellement selon le contexte.
    """
    def load_all_players(self) -> list[Player]:
        """Lit le fichier CSV et retourne la liste de tous les joueurs.

        Chaque ligne est convertie en objet Player. Les champs birthdate et player_api_id
        sont initialisés à None car ils ne sont pas présents dans le CSV source et doivent
        être renseignés manuellement.

        Returns:
            list[Player]: Liste des joueurs chargés.
                          Vide si le fichier l'est
        
        Raises:
            FileNotFoundError: Si le fichier CSV est introuvable
            KeyError: Si une colonne obligatoire est absente du CSV.
        """
        players_list = []
        with open('./data/football_champions_league/player.csv', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                player = Player(
                    nom=row["player_name"],
                    birthdate=None,
                    player_api_id=None
                )
                players_list.append(player)
        return players_list
import csv

from src.Model.Match import Match


class LoLMatchLoader:
    """Charge les données de matchs de League of Legends à partir d'un fichier CSV.
    
    Le fichier CSV doit contenir les colonnes gameid, date, team_blue, team_red, kills_team_blue, kills_team_red.
    """
    @staticmethod
    def load_all_matches() -> list[Match]:
        """Charge tous les matchs de League of Legends à partir du fichier CSV et les retourne sous forme de liste de Match.
        
        Returns:
            list[Match]: Une liste d'instances de Match représentant les matchs chargés.
        
        Raises:
            FileNotFoundError: Si le fichier CSV n'est pas trouvable.
            Exception: Si une erreur se produit
        """
        liste_matchs = []
        with open('./data/league_of_legends/match.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                match = Match(
                    match_id=row.get("gameid"),
                    date=row.get("date"),
                    team1=row.get("team_blue"),
                    team2=row.get("team_red"),
                    score1=int(row.get("kills_team_blue") or 0),
                    score2=int(row.get("kills_team_red") or 0),
                )
                liste_matchs.append(match)
        return liste_matchs
import csv
from src.Model.Match import Match

class CS2MatchLoader:
    """Classe pour charger les données de match de CS à partir d'un fichier CSV.
    
    Le fichier CSV doit avoir les colonnes suivantes date, team_1, team_2, score_team_1, score_team_2.
    L'identifiant du match est généré automatiquement et n'est pas présent dans le fichier CSV.
    Les scores sont nuls s'ils ne sont pas spécifiés dans le fichier CSV.
    """
    def load_all_matches(self) -> list[Match]:
        """Charge tous les matchs à partir du CSV et retourne une liste d'instances de Match.
        
        Returns:
            list[Match]: Une liste d'instances de Match contenant les données chargées du fichier CSV.
        Raises:
            FileNotFoundError: Si le fichier CSV n'est pas trouvable
            csv.Error: Si le fichier CSV est mal formé ou ne peut pas être lu
        """
        liste_matchs = []
        with open('./data/counter_strike_2/match.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                match = Match(
                    match_id=None,
                    date=row.get("date"),
                    team1=row.get("team_1"),
                    team2=row.get("team_2"),
                    score1=int(row.get("score_team_1") or 0),
                    score2=int(row.get("score_team_2") or 0),
                )
                liste_matchs.append(match)
        return liste_matchs

if __name__ == "__main__":
    matches = CS2MatchLoader().load_all_matches()
    for match in matches:
        print(match)
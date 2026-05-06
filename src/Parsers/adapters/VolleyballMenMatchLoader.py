import csv
from src.Model.Match import Match

class VolleyballMenMatchLoader:
    """Charge les données des matchs de volleyball masculin à partir d'un CSV
    
    Utilise les colonnes date, country_code_1, country_code_2, set_country_1 et set_country_2 du CSV
    pour créer des instances de Match
    """
    def load_all_matches(self) -> list[Match]:
        """ Transforme les données du CSV en une liste d'instances de Match
        
        Returns:
            list[Match]: une liste d'instances de Match créées à partir des données du CSV
        
        Raises:
            FileNotFoundError: si le fichier CSV n'est pas trouvable
            KeyError: si des colonnes sont manquantes"""
        liste_matchs = []
        with open('./data/volleyball/match_men.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                match = Match(
                    match_id=None,
                    date=row.get("date"),
                    team1=row.get("country_code_1"),
                    team2=row.get("country_code_2"),
                    score1=int(row.get("set_country_1") or 0),
                    score2=int(row.get("set_country_2") or 0),
                )
                liste_matchs.append(match)
        return liste_matchs

if __name__ == "__main__":
    matches = VolleyballMenMatchLoader().load_all_matches()
    for match in matches:
        print(match)
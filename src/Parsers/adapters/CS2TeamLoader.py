import csv
from src.Model.Team import Team

class CS2TeamLoader:
    """Charge les équipes de CS à partir d'un fichier CSV et les instancie en Team.
    
    Le fichier CSV doit avoir les colonnes team, team_abbreviation.
    """
    def load_all_teams(self) -> list[Team]:
        """Charge toutes les équipes de CS à partir du fichier CSV et les renvoie sous forme de liste de Team.
        
        Returns:
            list[Team]: La liste des équipes chargées.
        Raises:
            FileNotFoundError: Si le fichier CSV n'est pas trouvable.
            KeyError: Si les colonnes attendues ne sont pas présentes dans le CSV.
        """
        teams_list = []
        with open('./data/counter_strike_2/team.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                team = Team(
                    id=None,
                    nom=row.get('team'),
                    abreviation=row.get('team_abbreviation'),
                    competition_id=None,
                )
                teams_list.append(team)
        return teams_list
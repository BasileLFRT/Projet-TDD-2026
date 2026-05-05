import csv
from src.Model.Team import Team

class BasketballTeamLoader:
    """Classe permettant de charger des équipes NBA depuis un fichier CSV.

    Lit les données du fichier team.csv lié au basket et en crée des instances de Team
    avec les colonnes: id, full_name, abbreviation.
    Le champ competition_id est laissé à None au chargement
    et doit être assigné manuellement selon le contexte.
    """
    def load_all_teams(self) -> list[Team]:
        """Lit le fichier CSV et retourne la liste de toutes les équipes.

        Chaque ligne est convertie en objet Team. Le champ competition_id
        est initialisé à None car il n'est pas présent dans le CSV source
        et dépend de la compétition dans laquelle l'équipe est inscrite.
        Il est à renseigner manuellement.

        Returns:
            list[Team]: Liste des équipes chargées. 
                        Vide si le fichier ne contient aucune ligne de données.

        Raises:
            FileNotFoundError: Si le fichier CSV est introuvable 
            KeyError: Si une colonne obligatoire est absente du CSV.
        """
        teams_list = []
        with open('./data/basketball/team.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                team = Team(
                    id=row.get('id'),
                    nom=row.get('full_name'),
                    abreviation=row.get('abbreviation'),
                    competition_id=None,
                )
                teams_list.append(team)
        return teams_list
import csv
from src.Model.Team import Team

class ChampionsLeagueTeamLoader:
    """Classe pour charger les équipes de la Ligue des Champions à partir d'un fichier CSV.
   
    Lit les données du fichier team.csv lié au football (et à la Ligue des Champions) et en crée des instances de Team
    avec les colonnes: full_name, short_name.
    Les champs id et competition_id sont laissés à None au chargement
    et doivent être assignés manuellement
    """
    def load_all_teams(self) -> list[Team]:
        """
        Lit le fichier CSV et retourne la liste de toutes les équipes.

        Chaque ligne est transformée en instance de Team.
        Les champs id et
        competition_id sont initialisés à None car absents du CSV source:
        id doit être généré à l'insertion, competition_id dépend de la
        compétition dans laquelle l'équipe est inscrite.

        Returns:
            list[Team]: Liste des équipes chargées. 
                        Vide si le fichier l'est

        Raises:
            FileNotFoundError: Si le fichier CSV est introuvable
            KeyError: Si une colonne obligatoire est absente du CSV.
        """
        teams_list = []
        with open('./data/football_champions_league/team.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                team = Team(
                    id=None,
                    nom=row.get('full_name'),
                    abreviation=row.get('short_name'),
                    competition_id=None,
                )
                teams_list.append(team)
        return teams_list
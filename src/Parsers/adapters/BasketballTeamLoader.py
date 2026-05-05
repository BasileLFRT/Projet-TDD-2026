import csv
from src.Model.Team import Team

class BasketballTeamLoader:
    def load_all_teams(self) -> list[Team]:
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
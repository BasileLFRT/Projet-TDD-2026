import csv
from src.Model.Team import Team

class VolleyballWomenTeamLoader:
    def load_all_teams(self) -> list[Team]:
        teams_set = set()
        with open('./data/volleyball/match_women.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                teams_set.add(row['country_1'])
                teams_set.add(row['country_2'])
        return [Team(id=None, nom=t, abreviation=t, competition_id=None) for t in sorted(teams_set)]
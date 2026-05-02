from typing import List
from src.Model.Team import Team

class TeamSearch:
    def filter_teams_by_name(
        self, teams: List[Team], search_string: str
    ) -> List[Team]:
        return [team for team in teams if search_string.lower() in team.nom.lower()]
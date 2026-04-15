import datetime
class Match:

    def __init__(self, match_id: int, date:datetime, home_team:str, away_team:str, home_score:int, away_score:int):
        self.match_id = match_id
        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.home_score = home_score
        self.away_score = away_score

    def winner(self):
        if self.home_score > self.away_score:
            return self.home_team
        elif self.score2 > self.score1:
            return self.team2
        return None

    def __str__(self):
        return f"{self.date} | {self.team1} {self.score1} - {self.score2} {self.team2}"

    def __repr__(self):
        return (
            f"Match(date='{self.date}', "
            f"team1='{self.team1}', team2='{self.team2}', "
            f"score1={self.score1}, score2={self.score2}')"
        )

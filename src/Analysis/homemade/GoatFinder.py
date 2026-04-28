from src.Model.Player import Player
import csv

def find_the_goat(players: list[Player]):
    # Compter les victoires par joueur
    wins_count = {}

    with open("./data/football_european_leagues/match.csv", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            home_goals = int(row["home_team_goal"] or 0)
            away_goals = int(row["away_team_goal"] or 0)

            if home_goals > away_goals:
                winning_cols = [f"home_player_{i}" for i in range(1, 12)]
            elif away_goals > home_goals:
                winning_cols = [f"away_player_{i}" for i in range(1, 12)]
            else:
                continue

            for col in winning_cols:
                pid = row[col]
                if pid and pid.strip():
                    pid_clean = str(int(float(pid)))
                    wins_count[pid_clean] = wins_count.get(pid_clean, 0) + 1

    goat_id = max(wins_count, key=wins_count.get)
    goats = [p for p in players if str(p.player_api_id) == goat_id]

    if not len(goats) == 1:
        raise ValueError("There can only be one GOAT")
    return goats[0]

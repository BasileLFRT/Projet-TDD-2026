import pandas as pd
import matplotlib.pyplot as plt
import os
from src.Model.Competition import Competition
from src.Model.Sport import Sport

def show_score_evolution(matches_df: pd.DataFrame, sport: Sport, competition: Competition = None, nom_recherche = None):

    if sport.nom in ["chess", "badminton", "starcraft_2", "league_of_legends", "counter_strike_2"]:
        if sport.nom == "chess":
            players_df = pd.read_csv("./data/chess/player.csv")
            name_col = "name"
        elif sport.nom == "badminton":
            players_df = pd.read_csv("./data/badminton/player.csv")
            name_col = "name"
        elif sport.nom == "league_of_legends":
            players_df = pd.read_csv("./data/league_of_legends/player.csv")
            name_col = "pseudo"
        elif sport.nom == "counter_strike_2":
            players_df = pd.read_csv("./data/counter_strike_2/player.csv")
            name_col = "pseudo"
        else:  # starcraft_2
            players_df = pd.read_csv("./data/starcraft_2/player.csv")
            name_col = "pseudo"

        for i, row in players_df.iterrows():
            print(f"{i} - {row[name_col]}")
        index = int(input("Sélectionne un joueur (numéro) : "))
        player_name = players_df.iloc[index][name_col]

        if sport.nom == "chess":
            player_matches = matches_df[
                (matches_df["player_1"] == player_name) |
                (matches_df["player_2"] == player_name)
            ].copy()
            s1 = pd.to_numeric(player_matches["score_player_1"], errors='coerce')
            s2 = pd.to_numeric(player_matches["score_player_2"], errors='coerce')
            player_matches["win"] = ((player_matches["player_1"] == player_name) & (s1 > s2)) | \
                ((player_matches["player_2"] == player_name) & (s2 > s1))
        elif sport.nom == "badminton":
            player_matches = matches_df[
                (matches_df["player_1"] == player_name) |
                (matches_df["player_2"] == player_name)
            ].copy()
            player_matches["win"] = player_matches["winner"] == player_name
        elif sport.nom == "league_of_legends":
            blue_cols = ["top_team_blue", "jungle_team_blue", "mid_team_blue", "bot_team_blue", "sup_team_blue"]
            red_cols = ["top_team_red", "jungle_team_red", "mid_team_red", "bot_team_red", "sup_team_red"]
            player_matches = matches_df[matches_df[blue_cols + red_cols].isin([player_name]).any(axis=1)].copy()
            player_matches["win"] = (
                (player_matches[blue_cols].isin([player_name]).any(axis=1) & (player_matches["winner"] == player_matches["team_blue"])) |
                (player_matches[red_cols].isin([player_name]).any(axis=1) & (player_matches["winner"] == player_matches["team_red"]))
            )
        elif sport.nom == "counter_strike_2":
            team = players_df.iloc[index]["team"]
            player_matches = matches_df[
                (matches_df["team_1"] == team) | (matches_df["team_2"] == team)
            ].copy()
            player_matches["win"] = (
                ((player_matches["team_1"] == team) & (player_matches["score_team_1"] > player_matches["score_team_2"])) |
                ((player_matches["team_2"] == team) & (player_matches["score_team_2"] > player_matches["score_team_1"]))
            )
        else:  # starcraft_2
            player_matches = matches_df[
                (matches_df["player_1"] == player_name) |
                (matches_df["player_2"] == player_name)
            ].copy()
            s1 = pd.to_numeric(player_matches["score_player_1"], errors='coerce')
            s2 = pd.to_numeric(player_matches["score_player_2"], errors='coerce')
            player_matches["win"] = ((player_matches["player_1"] == player_name) & (s1 > s2)) | \
                ((player_matches["player_2"] == player_name) & (s2 > s1))

        if len(player_matches) == 0:
            print("Aucun match trouvé pour ce joueur.")
            return

        player_matches["win"] = player_matches["win"].astype(int)
        player_matches["cumulative_wins"] = player_matches["win"].cumsum()

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
        ax1.plot(range(len(player_matches)), player_matches["win"])
        ax1.set_title(f"Victoires par match — {player_name}")
        ax1.set_xlabel("Match")
        ax1.set_ylabel("Victoire (1) / Défaite (0)")
        ax2.plot(range(len(player_matches)), player_matches["cumulative_wins"])
        ax2.set_title(f"Victoires cumulées — {player_name}")
        ax2.set_xlabel("Match")
        ax2.set_ylabel("Total victoires")

        plt.tight_layout()
        os.makedirs('./output', exist_ok=True)
        plt.savefig('./output/score_evolution.png', dpi=100, bbox_inches='tight')
        plt.close()
        print("Graphique sauvegardé dans ./output/score_evolution.png")
        return

    if sport.nom == "tennis":
        players_df = pd.read_csv(f"./data/tennis/{competition.nom}_players_2024.csv")
        players_df["full_name"] = players_df["name_first"] + " " + players_df["name_last"]
        for i, row in players_df.iterrows():
            print(f"{i} - {row['full_name']}")
        index = int(input("Sélectionne un joueur (numéro) : "))
        player = players_df.iloc[index]
        player_id = str(player["player_id"])
        player_name = player["full_name"]

        matches_df["date"] = pd.to_datetime(matches_df["tourney_date"].astype(str))
        player_matches = matches_df[
            (matches_df["winner_id"].astype(str) == player_id) |
            (matches_df["loser_id"].astype(str) == player_id)
        ].sort_values("date")

        if len(player_matches) == 0:
            print("Aucun match trouvé pour ce joueur.")
            return

        player_matches["win"] = (player_matches["winner_id"].astype(str) == player_id).astype(int)
        player_matches["cumulative_wins"] = player_matches["win"].cumsum()

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
        ax1.plot(range(len(player_matches)), player_matches["win"])
        ax1.set_title(f"Victoires par match — {player_name}")
        ax1.set_xlabel("Match")
        ax1.set_ylabel("Victoire (1) / Défaite (0)")
        ax2.plot(range(len(player_matches)), player_matches["cumulative_wins"])
        ax2.set_title(f"Victoires cumulées — {player_name}")
        ax2.set_xlabel("Match")
        ax2.set_ylabel("Total victoires")

        plt.tight_layout()
        os.makedirs('./output', exist_ok=True)
        plt.savefig('./output/score_evolution.png', dpi=100, bbox_inches='tight')
        plt.close()
        print("Graphique sauvegardé dans ./output/score_evolution.png")
        return

    if competition and competition.nom == "european_leagues":
        teams_df = pd.read_csv("./data/football_european_leagues/team.csv")
        for i, row in teams_df.iterrows():
            print(f"{i} - {row['team_long_name']}")
        index = int(input("Sélectionne une équipe (numéro) : "))
        team_id = teams_df.iloc[index]["team_api_id"]
        team_name = teams_df.iloc[index]["team_long_name"]

        home = matches_df[matches_df["home_team_api_id"] == team_id][["date", "home_team_goal"]].rename(columns={"home_team_goal": "goals"})
        away = matches_df[matches_df["away_team_api_id"] == team_id][["date", "away_team_goal"]].rename(columns={"away_team_goal": "goals"})
        team_matches = pd.concat([home, away]).sort_values("date")
        team_matches["goals"] = team_matches["goals"].astype(int)
        team_matches["cumulative"] = team_matches["goals"].cumsum()

    elif competition and competition.nom == "champions_league":
        teams = sorted(set(matches_df["team_home"].tolist() + matches_df["team_away"].tolist()))
        for i, team in enumerate(teams):
            print(f"{i} - {team}")
        index = int(input("Sélectionne une équipe (numéro) : "))
        team_name = teams[index]

        home = matches_df[matches_df["team_home"] == team_name][["date", "score_team_home"]].rename(columns={"score_team_home": "goals"})
        away = matches_df[matches_df["team_away"] == team_name][["date", "score_team_away"]].rename(columns={"score_team_away": "goals"})
        team_matches = pd.concat([home, away]).sort_values("date")
        team_matches["goals"] = team_matches["goals"].astype(int)
        team_matches["cumulative"] = team_matches["goals"].cumsum()

    elif sport.nom == "basketball":
        teams_df = pd.read_csv("./data/basketball/team.csv")
        for i, row in teams_df.iterrows():
            print(f"{i} - {row['full_name']}")
        index = int(input("Sélectionne une équipe (numéro) : "))
        team_id = int(teams_df.iloc[index]["id"])
        team_name = teams_df.iloc[index]["full_name"]

        home = matches_df[matches_df["team_id_home"] == team_id][["game_date", "pts_home"]].rename(columns={"game_date": "date", "pts_home": "goals"})
        away = matches_df[matches_df["team_id_away"] == team_id][["game_date", "pts_away"]].rename(columns={"game_date": "date", "pts_away": "goals"})
        team_matches = pd.concat([home, away]).sort_values("date")
        team_matches["goals"] = team_matches["goals"].astype(int)
        team_matches["cumulative"] = team_matches["goals"].cumsum()

    elif sport.nom == "volleyball":
        if competition and competition.nom == "volleyball_men":
            teams = sorted(set(matches_df["country_code_1"].tolist() + matches_df["country_code_2"].tolist()))
        else:
            teams = sorted(set(matches_df["country_1"].tolist() + matches_df["country_2"].tolist()))
        for i, team in enumerate(teams):
            print(f"{i} - {team}")
        index = int(input("Sélectionne une équipe (numéro) : "))
        team_name = teams[index]

        if competition and competition.nom == "volleyball_men":
            home = matches_df[matches_df["country_code_1"] == team_name][["date", "set_country_1"]].rename(columns={"set_country_1": "goals"})
            away = matches_df[matches_df["country_code_2"] == team_name][["date", "set_country_2"]].rename(columns={"set_country_2": "goals"})
        else:
            home = matches_df[matches_df["country_1"] == team_name][["date", "set_country_1"]].rename(columns={"set_country_1": "goals"})
            away = matches_df[matches_df["country_2"] == team_name][["date", "set_country_2"]].rename(columns={"set_country_2": "goals"})
        team_matches = pd.concat([home, away]).sort_values("date")
        team_matches["goals"] = team_matches["goals"].astype(int)
        team_matches["cumulative"] = team_matches["goals"].cumsum()

    elif sport.nom == "counter_strike_2":
        teams = sorted(set(matches_df["team_1"].tolist() + matches_df["team_2"].tolist()))
        for i, team in enumerate(teams):
            print(f"{i} - {team}")
        index = int(input("Sélectionne une équipe (numéro) : "))
        team_name = teams[index]

        home = matches_df[matches_df["team_1"] == team_name][["date", "score_team_1"]].rename(columns={"score_team_1": "goals"})
        away = matches_df[matches_df["team_2"] == team_name][["date", "score_team_2"]].rename(columns={"score_team_2": "goals"})
        team_matches = pd.concat([home, away]).sort_values("date")
        team_matches["goals"] = team_matches["goals"].astype(int)
        team_matches["cumulative"] = team_matches["goals"].cumsum()

    elif sport.nom == "league_of_legends":
        teams = sorted(set(matches_df["team_blue"].tolist() + matches_df["team_red"].tolist()))
        for i, team in enumerate(teams):
            print(f"{i} - {team}")
        index = int(input("Sélectionne une équipe (numéro) : "))
        team_name = teams[index]

        home = matches_df[matches_df["team_blue"] == team_name][["date", "kills_team_blue"]].rename(columns={"kills_team_blue": "goals"})
        away = matches_df[matches_df["team_red"] == team_name][["date", "kills_team_red"]].rename(columns={"kills_team_red": "goals"})
        team_matches = pd.concat([home, away]).sort_values("date")
        team_matches["goals"] = team_matches["goals"].astype(int)
        team_matches["cumulative"] = team_matches["goals"].cumsum()

    else:
        raise ValueError("Fonctionnalité non disponible pour ce sport")

    if len(team_matches) == 0:
        print("Aucun match trouvé pour cette équipe.")
        return

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
    ax1.plot(range(len(team_matches)), team_matches["goals"])
    ax1.set_title(f"Buts/points par match — {team_name}")
    ax1.set_xlabel("Match")
    ax1.set_ylabel("Buts/points")
    ax2.plot(range(len(team_matches)), team_matches["cumulative"])
    ax2.set_title(f"Buts/points cumulés — {team_name}")
    ax2.set_xlabel("Match")
    ax2.set_ylabel("Total cumulé")

    plt.tight_layout()
    os.makedirs('./output', exist_ok=True)
    plt.savefig('./output/score_evolution.png', dpi=100, bbox_inches='tight')
    plt.close()
    print("Graphique sauvegardé dans ./output/score_evolution.png")
import pandas as pd
from src.Model.Competition import Competition
from src.Model.Sport import Sport

def show_best_match(matches_df: pd.DataFrame, sport: Sport, competition: Competition = None):
    if sport.nom == "tennis":
        #match avec le plus d'aces combinés
        matches_df["total_aces"] = matches_df["w_ace"] + matches_df["l_ace"]
        best = matches_df.loc[matches_df["total_aces"].idxmax()]
        print(f"Match avec le plus d'aces :")
        print(f"  {best['tourney_date']} | {best['tourney_name']} | {best['winner_id']} vs {best['loser_id']}")
        print(f"  Nombre total d'aces : {int(best['total_aces'])}")
        return

    if competition and competition.nom == "european_leagues":
        matches_df["total_goals"] = matches_df["home_team_goal"] + matches_df["away_team_goal"]
        best = matches_df.loc[matches_df["total_goals"].idxmax()]
        print(f"Match avec le plus de buts :")
        print(f"  {best['date']} | {best['home_team_api_id']} {int(best['home_team_goal'])} - {int(best['away_team_goal'])} {best['away_team_api_id']}")
        print(f"  Total de buts : {int(best['total_goals'])}")

    elif competition and competition.nom == "champions_league":
        matches_df["total_goals"] = matches_df["score_team_home"] + matches_df["score_team_away"]
        best = matches_df.loc[matches_df["total_goals"].idxmax()]
        print(f"Match avec le plus de buts :")
        print(f"  {best['date']} | {best['team_home']} {int(best['score_team_home'])} - {int(best['score_team_away'])} {best['team_away']}")
        print(f"  Total de buts : {int(best['total_goals'])}")

    elif sport.nom in ["chess", "starcraft_2"]:
        matches_df["score1"] = pd.to_numeric(matches_df["score_player_1"], errors='coerce').fillna(0)
        matches_df["score2"] = pd.to_numeric(matches_df["score_player_2"], errors='coerce').fillna(0)
        best = matches_df.loc[(matches_df["score1"] - matches_df["score2"]).abs().idxmax()]
        print(f"Match avec le plus grand écart :")
        print(f"  {best['player_1']} {best['score_player_1']} - {best['score_player_2']} {best['player_2']}")

    elif sport.nom == "badminton":
        matches_df["total_games"] = matches_df["game_1_score"].notna().astype(int) + matches_df["game_2_score"].notna().astype(int) + matches_df["game_3_score"].notna().astype(int)
        best = matches_df.loc[matches_df["total_games"].idxmax()]
        print(f"Match le plus long :")
        print(f"  {best['date']} | {best['player_1']} vs {best['player_2']}")
        print(f"  {best['game_1_score']} / {best['game_2_score']} / {best['game_3_score']}")

    else:  # basketball
        matches_df["total_points"] = matches_df["pts_home"] + matches_df["pts_away"]
        best = matches_df.loc[matches_df["total_points"].idxmax()]
        print(f"Match avec le plus de points :")
        print(f"  {best['game_date']} | {best['team_id_home']} {int(best['pts_home'])} - {int(best['pts_away'])} {best['team_id_away']}")
        print(f"  Total de points : {int(best['total_points'])}")
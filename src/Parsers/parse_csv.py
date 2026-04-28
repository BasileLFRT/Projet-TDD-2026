from src.Common.utils import print_timings
from .csv_importer import CsvImporter
from src.Model.Player import Player

@print_timings
def parse_players_csv(filepath: str, sep: str = ";") -> list:
    importer = CsvImporter(filepath)
    rows = importer.read()
    return [Player(nom=row["player_name"], birthdate=None, player_api_id=row["player_api_id"]) for row in rows]

@print_timings
def parse_teams_csv(filepath: str, sep: str = ";") -> list:
    pass

from src.Common.utils import print_timings
from .csv_importer import CsvImporter


@print_timings
def parse_players_csv(filepath: str, sep: str = ";") -> list:
    raise Exception(
        "Oh non, la méthode parce_csv n'a pas été implémentée, "
        "vous allez devoir le faire vous-mêmes :("
    )
    return list()

@print_timings
def parse_teams_csv(filepath: str, sep: str = ";") -> list:
    pass

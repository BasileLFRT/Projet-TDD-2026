import csv

class CsvImporter:
    """Permet de lire les fichiers csv extérieur
    
    Convertit les CSV en liste de dictionnaires,
    où chaque dict est une ligne de csv
    """
    def __init__(self, filepath: str):
        self.filepath = filepath

    def read(self) -> list[dict]:
        with open(self.filepath, newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))


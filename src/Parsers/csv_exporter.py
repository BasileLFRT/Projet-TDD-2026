import csv

class CsvExporter:
    """Permet d'écrire des fichiers csv extérieur
    
    Convertit une liste de dictionnaires en CSV,
    où chaque dict est une ligne de csv"""
    def __init__(self, filepath: str):
        self.filepath = filepath

    def write(self, data: list[dict]) -> None:
        if not data:
            return
        with open(self.filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
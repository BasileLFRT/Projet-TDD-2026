import csv

class CsvImporter:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def read(self) -> list[dict]:
        with open(self.filepath, newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))


import csv

class CsvImporter:
    def import_matches(self, filepath: str) -> list:
        matches = []
        with open(filepath, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # validation + création des objets Match
                matches.append(row)
        return matches
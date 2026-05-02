import csv

class CsvExporter:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def write(self, data: list[dict]) -> None:
        if not data:
            return
        with open(self.filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
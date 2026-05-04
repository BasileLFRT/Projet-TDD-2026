from src.Parsers.csv_exporter import CsvExporter
from src.Parsers.csv_importer import CsvImporter

def test_csv_exporter_writes_file_correctly(tmp_path):
    csv_file = tmp_path / "test.csv"
    data = [{"name": "Alice", "age": "30"}, {"name": "Bob", "age": "25"}]
    exporter = CsvExporter(str(csv_file))
    exporter.write(data)
    importer = CsvImporter(str(csv_file))
    result = importer.read()
    assert len(result) == 2
    assert result[0]["name"] == "Alice"
    assert result[1]["name"] == "Bob"

def test_csv_exporter_does_nothing_with_empty_data(tmp_path):
    csv_file = tmp_path / "test.csv"
    exporter = CsvExporter(str(csv_file))
    exporter.write([])
    assert not csv_file.exists()
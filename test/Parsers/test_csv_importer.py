from src.Parsers.csv_importer import CsvImporter

def test_csv_importer_reads_file_correctly(tmp_path):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("name,age\nAlice,30\nBob,25\n", encoding="utf-8")
    importer = CsvImporter(str(csv_file))
    result = importer.read()
    assert len(result) == 2
    assert result[0]["name"] == "Alice"
    assert result[1]["name"] == "Bob"

def test_csv_importer_returns_list_of_dicts(tmp_path):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("name,age\nAlice,30\n", encoding="utf-8")
    importer = CsvImporter(str(csv_file))
    result = importer.read()
    assert isinstance(result, list)
    assert isinstance(result[0], dict)
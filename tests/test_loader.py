from csv_to_sql.loader import load_csv_to_sqlite
import os

def test_load_csv_to_sqlite(tmp_path):
    csv_file = tmp_path / "test.csv"
    db_file = tmp_path / "test.db"

    csv_file.write_text("id,name\n1,Alice\n2,Bob\n")
    result = load_csv_to_sqlite(str(csv_file), str(db_file), "people")

    assert "Loaded 2 rows" in result
    assert os.path.exists(db_file)

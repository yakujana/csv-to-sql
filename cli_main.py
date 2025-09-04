import typer
import pandas as pd
import sqlite3

app = typer.Typer(help="CSV-to-SQL CLI")

def load_csv_to_sqlite(csv_file: str, db_file: str, table_name: str):
    df = pd.read_csv(csv_file)
    conn = sqlite3.connect(db_file)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    return f"Loaded {len(df)} rows into {table_name} in {db_file}"

@app.command()
def load(
    csv_file: str = typer.Option(..., "--csv-file", "-c", help="Path to CSV file"),
    db_file: str = typer.Option("data.db", "--db-file", "-d", help="SQLite DB file"),
    table_name: str = typer.Option("my_table", "--table-name", "-t", help="Table name")
):
    """
    Load a CSV file into a SQLite database.
    """
    result = load_csv_to_sqlite(csv_file, db_file, table_name)
    typer.echo(result)

if __name__ == "__main__":
    app()


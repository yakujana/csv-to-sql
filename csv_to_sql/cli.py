import typer
from csv_to_sql.loader import load_csv_to_sqlite

app = typer.Typer()

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


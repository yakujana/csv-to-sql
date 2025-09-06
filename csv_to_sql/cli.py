import typer
from csv_to_sql.loader import load_csv_to_sqlite

app = typer.Typer(help="CSV-to-SQL CLI")

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

<<<<<<< HEAD



=======
if __name__ == "__main__":
    app()
>>>>>>> 9c7220b464b3be1a6baae8bbed0f63f8d7f6bbeb


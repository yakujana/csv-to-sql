import typer
from .loader import load_csv_to_sqlite

app = typer.Typer()

@app.command()
def load(
    csv_file: str,  # positional argument
    db_file: str = "data.db",  # option with default
    table_name: str = "my_table"  # option with default
):
    """
    Load a CSV file into a SQLite database.
    """
    result = load_csv_to_sqlite(csv_file, db_file, table_name)
    typer.echo(result)

if __name__ == "__main__":
    app()


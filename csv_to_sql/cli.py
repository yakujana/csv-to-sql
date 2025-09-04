import typer
from .loader import load_csv_to_sqlite

app = typer.Typer()

@app.command()
def load(csv_file: str, db_file: str = "data.db", table_name: str = "my_table"):
    result = load_csv_to_sqlite(csv_file, db_file, table_name)
    typer.echo(result)

if __name__ == "__main__":
    app()

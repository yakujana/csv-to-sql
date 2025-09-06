import typer
import pandas as pd
import sqlite3

app = typer.Typer(help="A CLI tool to manage CSV data and SQLite databases.")

# --- The 'preview' command ---
@app.command()
def preview(
    csv_file: str = typer.Option(..., "--csv-file", "-c", help="Path to the CSV file"),
    rows: int = typer.Option(5, "--rows", "-r", help="Number of rows to preview")
):
    """
    Preview the first N rows of a CSV file.
    """
    try:
        df = pd.read_csv(csv_file)
        typer.echo(df.head(rows))
    except FileNotFoundError:
        typer.echo(f"Error: The file '{csv_file}' was not found.", err=True)

# --- The 'load' command ---
@app.command()
def load(
    csv_file: str = typer.Option(..., "--csv-file", "-c", help="Path to the CSV file"),
    db_file: str = typer.Option("data.db", "--db-file", "-d", help="SQLite DB file"),
    table_name: str = typer.Option("my_table", "--table-name", "-t", help="Table name")
):
    """
    Load a CSV file into a SQLite database.
    """
    try:
        df = pd.read_csv(csv_file)
        conn = sqlite3.connect(db_file)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.close()
        typer.echo(f"Successfully loaded {len(df)} rows into '{db_file}'.")
    except FileNotFoundError:
        typer.echo(f"Error: The file '{csv_file}' was not found.", err=True)
    except Exception as e:
        typer.echo(f"An error occurred: {e}", err=True)

# --- The 'stats' command ---
@app.command()
def stats(
    csv_file: str = typer.Option(..., "--csv-file", "-c", help="Path to the CSV file")
):
    """
    Compute basic statistics for all numeric columns in a CSV file.
    """
    try:
        df = pd.read_csv(csv_file)
        numeric_df = df.select_dtypes(include=['number'])
        if numeric_df.empty:
            typer.echo("No numeric columns found to analyze.")
            return

        description = numeric_df.describe().loc[['count', 'mean', 'min', 'max']].T
        typer.echo(description.to_markdown())

    except FileNotFoundError:
        typer.echo(f"Error: The file '{csv_file}' was not found.", err=True)
    except Exception as e:
        typer.echo(f"An error occurred: {e}", err=True)

if __name__ == "__main__":
    app()

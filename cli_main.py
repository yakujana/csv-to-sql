import typer
import pandas as pd
import sqlite3

print("CLI script is starting...")

# This is the single, correct way to create the main Typer application.
# It acts as the central hub for all your commands.
app = typer.Typer(help="CLI for managing CSV and SQLite files.")

# --- Preview Command ---
# The @app.command() decorator registers the function below as a CLI command.
@app.command()
def preview(
    # Typer.Option defines the command-line options for this function.
    # The '...' indicates that this option is required.
    csv_file: str = typer.Option(..., "--csv-file", "-c", help="Path to CSV file"),
    # This option has a default value of 5.
    rows: int = typer.Option(5, "--rows", "-r", help="Number of rows to preview")
):
    """
    Preview the first N rows of a CSV file.
    """
    print(f"Executing preview command on file: {csv_file}")
    try:
        # pandas.read_csv() reads the data from the specified CSV file.
        df = pd.read_csv(csv_file)
        # pandas.head() returns the first 'N' rows of the DataFrame.
        typer.echo(df.head(rows))
    except FileNotFoundError:
        typer.echo(f"Error: The file '{csv_file}' was not found.", err=True)
    except Exception as e:
        typer.echo(f"An error occurred: {e}", err=True)

# --- Load Command ---
@app.command()
def load(
    csv_file: str = typer.Option(..., "--csv-file", "-c", help="Path to CSV file"),
    db_file: str = typer.Option("data.db", "--db-file", "-d", help="SQLite DB file"),
    table_name: str = typer.Option("my_table", "--table-name", "-t", help="Table name")
):
    """
    Load a CSV file into a SQLite database.
    """
    print(f"Executing load command for file: {csv_file}")
    try:
        # Read the CSV into a pandas DataFrame.
        df = pd.read_csv(csv_file)
        # Connect to the SQLite database. If the file doesn't exist, it will be created.
        conn = sqlite3.connect(db_file)
        # The to_sql() method writes the DataFrame to a table in the database.
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        # Close the connection to the database.
        conn.close()
        typer.echo(f"Successfully loaded {len(df)} rows.")
    except FileNotFoundError:
        typer.echo(f"Error: The file '{csv_file}' was not found.", err=True)
    except Exception as e:
        typer.echo(f"An error occurred: {e}", err=True)

# --- Stats Command (NEW) ---
@app.command()
def stats(
    csv_file: str = typer.Option(..., "--csv-file", "-c", help="Path to CSV file")
):
    """
    Compute basic statistics for all numeric columns in a CSV file.
    """
    print(f"Executing stats command for file: {csv_file}")
    try:
        # Read the CSV into a pandas DataFrame.
        df = pd.read_csv(csv_file)
        # select_dtypes() filters the DataFrame to include only columns with a numeric data type.
        numeric_df = df.select_dtypes(include=['number'])
        if numeric_df.empty:
            typer.echo("No numeric columns found to analyze.")
            return

        # The describe() method generates descriptive statistics.
        description = numeric_df.describe().loc[['count', 'mean', 'min', 'max']].T
        # to_markdown() formats the output nicely for the command line.
        typer.echo(description.to_markdown())

    except FileNotFoundError:
        typer.echo(f"Error: The file '{csv_file}' was not found.", err=True)
    except Exception as e:
        typer.echo(f"An error occurred: {e}", err=True)


# The main entry point for the CLI.
# This must be at the end of the script and only appear once.
if __name__ == "__main__":
    app()

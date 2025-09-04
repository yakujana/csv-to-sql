# CSV-to-SQL Loader

A simple CLI tool to load CSV files into a SQLite database.

## Install
poetry install  # or pip install pandas typer pytest

## Usage
python -m csv_to_sql.cli load data.csv --db-file my.db --table-name sales

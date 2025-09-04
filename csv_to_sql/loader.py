import sqlite3
import pandas as pd

def load_csv_to_sqlite(csv_file: str, db_file: str, table_name: str):
    df = pd.read_csv(csv_file)
    conn = sqlite3.connect(db_file)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    return f"Loaded {len(df)} rows into {table_name} in {db_file}"

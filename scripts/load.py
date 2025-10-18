import pandas as pd
import sqlite3
import os

def load():
    csv_file = "output/retail_summary.csv"
    db_file = "output/retail.db"

    df = pd.read_csv(csv_file)
    conn = sqlite3.connect(db_file)
    df.to_sql("retail_summary", conn, if_exists="replace", index=False)
    conn.close()

    print(f"[LOAD] Summary loaded into SQLite database: {db_file}")

if __name__ == "__main__":
    load()

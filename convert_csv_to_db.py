import sqlite3
import pandas as pd

db_path = "glyph.csv"

conn = sqlite3.connect("glyphs.db")  # Provide a desired database name

# Read CSV file into a pandas DataFrame
df = pd.read_csv(db_path)
table_name = 'image_glyphs'

# Write the DataFrame to the SQLite database
df.to_sql(table_name, conn, index=False, if_exists='replace')

conn.close()

# df = pd.read_csv("/content/sample_data/glyph.csv")
# display(df.head())

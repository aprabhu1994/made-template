import pandas as pd
import sqlite3

# Step 1: Download the data
url = "https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv"
df = pd.read_csv(url, sep=";", encoding='ISO-8859-1', skiprows=6, skipfooter=4, engine='python')


# Step 2: Reshape the data structure
df = df.iloc[:, [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]]
df.columns = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

# Step 3: Validate data
# Validate CINs
df['CIN'] = df['CIN'].astype(str).str.zfill(5)

# Validate positive integers
numeric_columns = ['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')
df = df[df[numeric_columns] > 0]

# Step 4: Use fitting SQLite types
# Define SQLite types
sqlite_types = {'date': 'TEXT', 'CIN': 'TEXT', 'name': 'TEXT',
                'petrol': 'INTEGER', 'diesel': 'INTEGER', 'gas': 'INTEGER',
                'electro': 'INTEGER', 'hybrid': 'INTEGER', 'plugInHybrid': 'INTEGER', 'others': 'INTEGER'}

# Step 5: Write data to SQLite database
conn = sqlite3.connect('cars.sqlite')
df.to_sql('cars', conn, index=False, if_exists='replace', dtype=sqlite_types)
conn.close()

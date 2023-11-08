import pandas as pd
from sqlalchemy import create_engine, Integer, Text, Float

url = 'https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv'
path = 'airports.sqlite'

# Get data from url
airport_data = pd.read_csv(url, sep=';')

# Create a dictionary to define SQLite types for the DataFrame columns
column_types = {
    "column_1": Integer(),
    "column_2": Text(),
    "column_3": Text(),
    "column_4": Text(),
    "column_5": Text(),
    "column_6": Text(),
    "column_7": Float(),
    "column_8": Float(),
    "column_9": Integer(),
    "column_10": Float(),
    "column_11": Text(),
    "column_12": Text(),
    "geo_punkt": Text()
}

# Create a SQLAlchemy engine
engine = create_engine('sqlite:///' + path)

# Write the data to the SQLite database
airport_data.to_sql('airports', con=engine, if_exists='replace', index=False, dtype=column_types)
print("Data written successfully to 'airports.sqlite'.")

# Close the database connection
engine.dispose()

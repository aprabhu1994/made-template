import opendatasets as od
import sqlite3
import pandas as pd

#Testing Github actions ######

hotel_booking_dataset = 'https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand/download?datasetVersionNumber=1'

airbnb_dataset = 'https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data/download?datasetVersionNumber=3'

od.download(hotel_booking_dataset)

file_path = 'hotel-booking-demand/hotel_bookings.csv'
hotelbooking_df = pd.read_csv(file_path)
db_path1 = '../data/hotel_bookings.sqlite'
conn = sqlite3.connect(db_path1)
hotelbooking_df.to_sql('hotel_bookings', conn, index=False, if_exists='replace')
print("Database Created And stored at /data/hotel_bookings.sqlite")


od.download(airbnb_dataset)

file_path = 'new-york-city-airbnb-open-data/AB_NYC_2019.csv'
airbnb_df = pd.read_csv(file_path)
db_path2 = '../data/airbnb.sqlite'
conn = sqlite3.connect(db_path2)
airbnb_df.to_sql('airbnb', conn, index=False, if_exists='replace')
print("Database Created And stored at /data/airbnb.sqlite")

conn.close()

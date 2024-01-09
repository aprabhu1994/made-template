import opendatasets as od
import sqlite3
import pandas as pd
import numpy as np

hotel_booking_dataset = 'https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand/download?datasetVersionNumber=1'

airbnb_dataset = 'https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data/download?datasetVersionNumber=3'

od.download(hotel_booking_dataset)

file_path = 'hotel-booking-demand/hotel_bookings.csv'
hotelbooking_df = pd.read_csv(file_path)

# selecting columns which are relevant for pricing
price_columns_hotel = ['hotel', 'arrival_date_month', 'lead_time', 'adr', 'adults']
subset_hotel = hotelbooking_df[price_columns_hotel].copy()

# Calculate quartiles
Q1 = np.percentile(subset_hotel['adr'], 25)
Q3 = np.percentile(subset_hotel['adr'], 75)
IQR = Q3 - Q1

# Outlier detection
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers
hotel_df_filtered = subset_hotel.loc[(subset_hotel['adr'] > lower_bound) & (subset_hotel['adr'] < upper_bound)]

db_path1 = '../data/hotel_bookings.sqlite'
conn = sqlite3.connect(db_path1)
hotel_df_filtered.to_sql('hotel_bookings', conn, index=False, if_exists='replace')
print("Database Created And stored at /data/hotel_bookings.sqlite")


od.download(airbnb_dataset)

file_path = 'new-york-city-airbnb-open-data/AB_NYC_2019.csv'
airbnb_df = pd.read_csv(file_path)

# selecting columns which are relevant for pricing
price_columns_airbnb = ['neighbourhood_group', 'room_type', 'price', 'availability_365', 'number_of_reviews']
subset_airbnb = airbnb_df[price_columns_airbnb].copy()

# Calculate quartiles
Q1 = np.percentile(subset_airbnb['price'], 25)
Q3 = np.percentile(subset_airbnb['price'], 75)
IQR = Q3 - Q1

# Outlier detection
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Remove outliers
airbnb_df_filtered = subset_airbnb.loc[(subset_airbnb['price'] > lower_bound) & (subset_airbnb['price'] < upper_bound)]


db_path2 = '../data/airbnb.sqlite'
conn = sqlite3.connect(db_path2)
airbnb_df_filtered.to_sql('airbnb', conn, index=False, if_exists='replace')
print("Database Created And stored at /data/airbnb.sqlite")

conn.close()

import unittest
import os
import sqlite3
import pandas as pd


class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        print("Setting up test environment...")
        try:
            # Set up SQLite databases
            self.db_path1 = '../data/hotel_bookings.sqlite'
            self.conn1 = sqlite3.connect(self.db_path1)
            self.query1 = f"SELECT * FROM hotel_bookings;"
            self.hotelbooking_df = pd.read_sql_query(self.query1, self.conn1)

            self.db_path2 = '../data/airbnb.sqlite'
            self.conn2 = sqlite3.connect(self.db_path2)
            self.query2 = f"SELECT * FROM airbnb;"
            self.airbnb_df = pd.read_sql_query(self.query2, self.conn2)
        except Exception as e:
            self.fail(f"Failed to set up test environment: {e}")

    def test_hotel_bookings_database(self):
        print("Running hotel_bookings_database...")
        try:
            # Test if the hotel_bookings table exists in the database
            cursor = self.conn1.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            table_names = [table[0] for table in tables]
            self.assertIn('hotel_bookings', table_names)
            print("Test passed: hotel_bookings table exists in the database.")
        except Exception as e:
            self.fail(f"Test failed: {e}")

    def test_airbnb_database(self):
        print("Running airbnb_database...")
        try:
            # Test if the airbnb table exists in the database
            cursor = self.conn2.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            table_names = [table[0] for table in tables]
            self.assertIn('airbnb', table_names)
            print("Test passed: airbnb table exists in the database.")
        except Exception as e:
            self.fail(f"Test failed: {e}")

    def test_hotel_bookings_dataframe(self):
        print("Running test_hotel_bookings_dataframe...")
        try:
            # Test if the hotelbooking_df DataFrame is not empty
            self.assertFalse(self.hotelbooking_df.empty)
            print("Test passed: hotelbooking_df DataFrame is not empty.")
        except Exception as e:
            self.fail(f"Test failed: {e}")

    def test_airbnb_dataframe(self):
        print("Running test_airbnb_dataframe...")
        try:
            # Test if the airbnb_df DataFrame is not empty
            self.assertFalse(self.airbnb_df.empty)
            print("Test passed: airbnb_df DataFrame is not empty.")
        except Exception as e:
            self.fail(f"Test failed: {e}")


if __name__ == '__main__':
    unittest.main()

# import sys
# import os

# # Add the project root directory to the Python path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# import pandas as pd
# import mysql.connector
# from etl.config import DB_CONFIG

# def fetch_data_from_db():
#     """
#     Fetch data from the MySQL database and return it as a pandas DataFrame.
#     """
#     connection = mysql.connector.connect(**DB_CONFIG)
#     query = "SELECT * FROM daily_prices"
#     data = pd.read_sql(query, connection)
#     connection.close()
#     return data

# # Fetch data using the function
# data = fetch_data_from_db()
# print("Fetched data:", data.head())  # Add this line to check data

# import mysql.connector
# from etl.config import DB_CONFIG

# try:
#     connection = mysql.connector.connect(**DB_CONFIG)
#     print("Database connection successful!")
#     connection.close()
# except mysql.connector.Error as err:
#     print(f"Database connection failed: {err}")

import pandas as pd
import mysql.connector
from etl.config import DB_CONFIG

def fetch_data_from_db():
    """
    Fetch data from the MySQL database and return it as a pandas DataFrame.
    """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        query = "SELECT * FROM daily_prices"
        data = pd.read_sql(query, connection)
        connection.close()
        return data
    except mysql.connector.Error as err:
        print(f"Database connection failed: {err}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

# Fetch data using the function
data = fetch_data_from_db()
print("Fetched data:", data.head())  # Add this line to check data




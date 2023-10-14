import mysql.connector
import pandas as pd
import hashlib

class MySQLConnection:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def __enter__(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

# Set database connection parameters
HOST = "127.0.0.1"
DATABASE = "NITTANY"
USER = "root"
PASSWORD = "password123"

# Create database connection using context manager
with MySQLConnection(HOST, DATABASE, USER, PASSWORD) as db_connection:
    # Create a cursor object
    cursor = db_connection.cursor()
    print("Connected to:", db_connection.get_server_info())

    # Read data from CSV file
    csv_file_path = r"/Users/kishorpallod/Downloads/lionproject/LionAuctionDataset-v5/Users.csv"
    csvreader = pd.read_csv(csv_file_path)

    # Hash password column values
    csvreader['password'] = csvreader['password'].apply(lambda x: hashlib.sha256(x.encode()).hexdigest())

    # Insert data into MySQL table
    query = """INSERT INTO Users (email, password) VALUES (%s, %s)"""
    for ind in csvreader.index:
        tuple = (csvreader['email'][ind], csvreader['password'][ind])
        cursor.execute(query, tuple)
    db_connection.commit()

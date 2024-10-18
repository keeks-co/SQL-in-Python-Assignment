

import mysql.connector
from mysql.connector import Error

def connect_database():
    """ Connect to the MySql database and return the connection object """
    # Database connection parameters
    db_name = "e_commerce_db"
    user = "root"
    password = "your_password"
    host = "localhost"

    try:
        conn = mysql.connector.connect(
            database = "FitnessCenter_db",
            user = "root",
            password = "Kaa4@sql",
            host = "localhost"
            )
    
        print("Connected to mySQL database successfully")
        return conn

    except Error as e: 
        print(f"Error: {e}")
        return None
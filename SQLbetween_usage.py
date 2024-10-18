
from connect_db import connect_database

conn = connect_database()

def members_in_age_range(start_age, end_age):
    if conn is not None:
        cursor = conn.cursor()
        age_range = (start_age, end_age)
        query = "SELECT * FROM Members WHERE age BETWEEN %s AND %s;"
        cursor.execute(query, age_range)

        for row in cursor.fetchall():
            print(row)

members_in_age_range(25, 30)
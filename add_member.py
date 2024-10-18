
from connect_db import connect_database

conn = connect_database()

def add_member(id, name, age):
    if conn is not None:
        try:
            cursor = conn.cursor()
            new_member = (id, name, age)
            query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
            cursor.execute(query, new_member)
            conn.commit()
            print("New member successfully added.")

            
        except Exception as e:
            if "SELECT * FROM Members GROUP BY id HAVING COUNT(*) > 1 ":
                print(f"Duplicate Error: {e}")


add_member(290, "Liz Gray", 29)


def add_workout_session(member_id, date, duration_minutes, calories_burned):
    if conn is not None:
        try:
            cursor = conn.cursor()
            new_session = (member_id, date, duration_minutes, calories_burned)
            query = "INSERT INTO Members (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, new_session)
            conn.commit()
            print("New workout sessino has been added.")

        except Exception as e:
            if "SELECT member_id FROM WorkoutSessions NOT IN Members":
                print("Error: Member_id not valid.")
      

add_workout_session(12, "2024-11-04", "90", "200")





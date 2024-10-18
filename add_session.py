
from connect_db import connect_database

conn = connect_database()

def add_workout_session(session_id, member_id, session_date, session_time, activity):
    if conn is not None:
        try:
            cursor = conn.cursor()
            new_session = (session_id, member_id, session_date, session_time, activity)
            query = "INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, new_session)
            conn.commit()
            print("New workout session has been added.")

        except Exception as e:
            if "SELECT member_id FROM WorkoutSessions NOT IN Members": 
                print("Member_id not valid")
      

add_workout_session(5, 290, "2024-11-04", "Afternoon", "Zumba")
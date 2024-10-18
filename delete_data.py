
from connect_db import connect_database

conn = connect_database()

def delete_workout_session(session_id):
    if conn is not None:
        try:
            cursor = conn.cursor()
            query_1 = "SELECT session_id FROM WorkoutSessions WHERE NOT EXISTS (SELECT id FROM Members WHERE Members.id = session_id);" 
            session_id = (session_id, )
            query = " DELETE FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(query, session_id)
            conn.commit()
            print("Session has been cancelled.")
        except Exception as e:
            print(f"Error: {e}")
            #print("Error: Session ID does not exist")

delete_workout_session(5, )
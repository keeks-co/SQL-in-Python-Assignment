
from connect_db import connect_database

conn = connect_database()

def update_member_age(age, id):
    if conn is not None:
        try:
            cursor = conn.cursor()
            new_age = (age, id)
            query_1 = "SELECT id FROM Members WHERE EXISTS (SELECT member_id FROM WorkoutSessions WHERE Members.id = member_id);" #trying to check for if member id exists
            #cursor.execute(query_1)
            #print("Member id has been found.")

            query = "UPDATE Members SET age = %s WHERE id = %s" 
            cursor.execute(query, new_age)
            conn.commit()
            print("Member new age updated.")
   
        except Exception as e:
            print(f"Error: {e} has occured.")

update_member_age(31, 290)


 
           
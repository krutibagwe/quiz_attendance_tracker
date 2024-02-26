import mysql.connector

class DatabaseOperation:
    def __init__(self):
        # Replace these values with your actual MySQL database credentials
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'kRuti05!@21',
            'database': 'quizdatabase1'
        }

    def add_student(self, student_id, student_name, password):
        try:
            # Connect to the database
            connection = mysql.connector.connect(**self.db_config)

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Define the SQL query to insert student data into the table
            insert_query = "INSERT INTO students (student_id, student_name, password) VALUES (%s, %s, %s)"

            # Execute the query with actual values
            cursor.execute(insert_query, (student_id, student_name, password))

            # Commit the changes to the database
            connection.commit()

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()

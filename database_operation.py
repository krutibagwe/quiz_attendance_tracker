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

    def add_student(self, student_id, student_name, student_department, student_year, student_password):
        try:
            # Connect to the database
            connection = mysql.connector.connect(**self.db_config)

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Define the SQL query to insert student data into the table
            insert_query = "INSERT INTO students (student_id, student_name, student_department, student_year, student_password) VALUES (%s, %s, %s, %s, %s)"

            # Execute the query with actual values
            cursor.execute(insert_query, (student_id, student_name, student_department, student_year, student_password))

            # Commit the changes to the database
            connection.commit()

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()

    def add_teacher(self, teacher_id, teacher_name, password):
        try:
            # Connect to the database
            connection = mysql.connector.connect(**self.db_config)

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Define the SQL query to insert teacher data into the table
            insert_query = "INSERT INTO teachers (teacher_id, teacher_name, password) VALUES (%s, %s, %s)"

            # Execute the query with actual values
            cursor.execute(insert_query, (teacher_id, teacher_name, password))

            # Commit the changes to the database
            connection.commit()

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()


    def validate_student_login(self, student_id, student_password):
        connection = None
        cursor = None

        try:
            # Connect to the database
            connection = mysql.connector.connect(**self.db_config)

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Define the SQL query to check if student ID and password match
            select_query = "SELECT * FROM students WHERE student_id = %s AND student_password = %s"

            # Execute the query with actual values
            cursor.execute(select_query, (student_id, student_password))

            # Fetch the result
            result = cursor.fetchone()

            return result is not None  # If result is not None, login is successful

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()
                
    def validate_teacher_login(self, teacher_id, password):
        connection = None
        cursor = None

        try:
            # Connect to the database
            connection = mysql.connector.connect(**self.db_config)

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Define the SQL query to check if teacher ID and password match
            select_query = "SELECT * FROM teachers WHERE teacher_id = %s AND password = %s"

            # Execute the query with actual values
            cursor.execute(select_query, (teacher_id, password))

            # Fetch the result
            result = cursor.fetchone()

            return result is not None  # If result is not None, login is successful

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def add_question(self, subject, question_text, option_a, option_b, option_c, option_d, correct_option):
        connection = None
        cursor = None

        try:
            # Connect to the database
            connection = mysql.connector.connect(**self.db_config)

            # Create a cursor object to execute SQL queries
            cursor = connection.cursor()

            # Define the SQL query to insert a new question
            insert_query = "INSERT INTO questions (subject, question_text, option_a, option_b, option_c, option_d, correct_option) VALUES (%s, %s, %s, %s, %s, %s, %s)"

            # Execute the query with actual values
            cursor.execute(insert_query, (subject, question_text, option_a, option_b, option_c, option_d, correct_option))

            # Commit the changes to the database
            connection.commit()

        except mysql.connector.Error as e:
            # Handle any database errors here
            print(f"Error: {e}")
            connection.rollback()

        finally:
            # Close the cursor and connection
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_quiz_questions(self, subject, num_questions=10):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            query = "SELECT question_text, option_a, option_b, option_c, option_d, correct_option FROM questions WHERE subject = %s LIMIT %s"
            cursor.execute(query, (subject, num_questions))
            questions = cursor.fetchall()

            return questions

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            connection.close()
'''
import mysql.connector

class DatabaseOperation:
    def __init__(self):
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'kRuti05!@21',
            'database': 'quizdatabase1'
        }

    def add_student(self, student_id, student_name, student_department, student_year, student_password):
         try:
             connection = mysql.connector.connect(**self.db_config)
   
             cursor = connection.cursor()

             if not student_id:
                 raise ValueError("Student ID cannot be empty")

             insert_query = "INSERT INTO students (student_id, student_name, student_department, student_year, student_password) VALUES (%s, %s, %s, %s, %s)"

             cursor.execute(insert_query, (student_id, student_name, student_department, student_year, student_password))

             connection.commit()

             print("Student added successfully")

         except mysql.connector.Error as e:
            if e.errno == 1062:       
                print("Error: Duplicate student ID. Please enter a unique student ID.") 
        
            
            else:
                 print(f"Error: {e}")
           

         except ValueError as ve:
             print(f"Error: {ve}")
        

         finally:
          cursor.close()
          connection.close()


    def add_teacher(self, teacher_id, teacher_name, password):
        try:
            connection = mysql.connector.connect(**self.db_config)

            cursor = connection.cursor()

            insert_query = "INSERT INTO teachers (teacher_id, teacher_name, password) VALUES (%s, %s, %s)"

            cursor.execute(insert_query, (teacher_id, teacher_name, password))

            connection.commit()

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            connection.close()


    def validate_student_login(self, student_id, student_password):
        connection = None
        cursor = None

        try:
            connection = mysql.connector.connect(**self.db_config)

            cursor = connection.cursor()

            select_query = "SELECT * FROM students WHERE student_id = %s AND student_password = %s"

            cursor.execute(select_query, (student_id, student_password))

            result = cursor.fetchone()

            return result is not None  

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
                
    def validate_teacher_login(self, teacher_id, password):
        connection = None
        cursor = None

        try:
            connection = mysql.connector.connect(**self.db_config)

            cursor = connection.cursor()

            select_query = "SELECT * FROM teachers WHERE teacher_id = %s AND password = %s"

            cursor.execute(select_query, (teacher_id, password))

            result = cursor.fetchone()

            return result is not None  

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def add_question(self, subject, question_text, option_a, option_b, option_c, option_d, correct_option):
        connection = None
        cursor = None

        try:
            connection = mysql.connector.connect(**self.db_config)

            cursor = connection.cursor()

            insert_query = "INSERT INTO questions (subject, question_text, option_a, option_b, option_c, option_d, correct_option) VALUES (%s, %s, %s, %s, %s, %s, %s)"

            cursor.execute(insert_query, (subject, question_text, option_a, option_b, option_c, option_d, correct_option))

            connection.commit()

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            connection.rollback()

        finally:
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

    def add_score(self, student_id, subject, score):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()
    
            insert_query = "INSERT INTO scores (student_id, subject, score) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (student_id, subject, score))
        
            # Debug prints
            print(f"Student ID: {student_id}")
            print(f"Subject: {subject}")
            print(f"Score: {score}")
            print("Insertion query executed")

            connection.commit()
            print("Score added successfully")

        except mysql.connector.Error as e:
            print(f"Error: {e}")
        
            connection.rollback()

        finally:
            if cursor:
                cursor.close()
                '''


import mysql.connector

class DatabaseOperation:
    def __init__(self):
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'kRuti05!@21',
            'database': 'quizdatabase1'
        }

    def add_student(self, student_id, student_name, student_department, student_year, student_password):
         try:
             connection = mysql.connector.connect(**self.db_config)
   
             cursor = connection.cursor()

             if not student_id:
                 raise ValueError("Student ID cannot be empty")

             insert_query = "INSERT INTO students (student_id, student_name, student_department, student_year, student_password) VALUES (%s, %s, %s, %s, %s)"

             cursor.execute(insert_query, (student_id, student_name, student_department, student_year, student_password))

             connection.commit()

             print("Student added successfully")

         except mysql.connector.Error as e:
            if e.errno == 1062:       
                print("Error: Duplicate student ID. Please enter a unique student ID.") 
        
            
            else:
                 print(f"Error: {e}")
           

         except ValueError as ve:
             print(f"Error: {ve}")
        

         finally:
          cursor.close()
          connection.close()


    def add_teacher(self, teacher_id, teacher_name, password):
        try:
            connection = mysql.connector.connect(**self.db_config)

            cursor = connection.cursor()

            insert_query = "INSERT INTO teachers (teacher_id, teacher_name, password) VALUES (%s, %s, %s)"

            cursor.execute(insert_query, (teacher_id, teacher_name, password))

            connection.commit()

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            connection.close()


    def validate_student_login(self, student_id, student_password):
        connection = None
        cursor = None

        try:
            connection = mysql.connector.connect(**self.db_config)

            cursor = connection.cursor()

            select_query = "SELECT * FROM students WHERE student_id = %s AND student_password = %s"

            cursor.execute(select_query, (student_id, student_password))

            result = cursor.fetchone()

            return result is not None  

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
                
    def validate_teacher_login(self, teacher_id, password):
        connection = None
        cursor = None

        try:
            connection = mysql.connector.connect(**self.db_config)

            cursor = connection.cursor()

            select_query = "SELECT * FROM teachers WHERE teacher_id = %s AND password = %s"

            cursor.execute(select_query, (teacher_id, password))

            result = cursor.fetchone()

            return result is not None  

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def add_question(self, subject, question_text, option_a, option_b, option_c, option_d, correct_option):
        connection = None
        cursor = None

        try:
            connection = mysql.connector.connect(**self.db_config)

            cursor = connection.cursor()

            insert_query = "INSERT INTO questions (subject, question_text, option_a, option_b, option_c, option_d, correct_option) VALUES (%s, %s, %s, %s, %s, %s, %s)"

            cursor.execute(insert_query, (subject, question_text, option_a, option_b, option_c, option_d, correct_option))

            connection.commit()

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            connection.rollback()

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_quiz_questions(self, subject, num_questions=10):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()
            query = "SELECT question_text, option_a, option_b, option_c, option_d, correct_option FROM questions WHERE subject = %s ORDER BY RAND() LIMIT %s"
            cursor.execute(query, (subject, num_questions))
            questions = cursor.fetchall()

            return questions

        except mysql.connector.Error as e:
            print(f"Error: {e}")
        

        finally:
            cursor.close()
            connection.close()


    def add_score(self, student_id, subject, score, quiz_date):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            insert_query = "INSERT INTO scores (student_id, subject, score, quiz_date) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (student_id, subject, score, quiz_date))

            # Check if the score is 6 or more to mark attendance
            attendance = 'present' if score >= 6 else 'absent'
            update_query = "UPDATE scores SET attendance = %s WHERE student_id = %s AND subject = %s"
            cursor.execute(update_query, (attendance, student_id, subject))

            connection.commit()
            print("Score added successfully")
        
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            connection.rollback()

        finally:
            if cursor:
                cursor.close()

        
            
    def get_student_subject_stats(self, student_id, subject):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            select_query = "SELECT COUNT(*) FROM quiz_answers WHERE student_id = %s AND subject = %s AND is_correct = 1"
            cursor.execute(select_query, (student_id, subject))
            correct_count = cursor.fetchone()[0]

            select_query = "SELECT COUNT(*) FROM quiz_answers WHERE student_id = %s AND subject = %s AND is_correct = 0"
            cursor.execute(select_query, (student_id, subject))
            incorrect_count = cursor.fetchone()[0]

            return correct_count, incorrect_count

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

        
            
            




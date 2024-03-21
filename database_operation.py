
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

            # Insert the score record
            insert_query = "INSERT INTO scores (student_id, subject, score, quiz_date) VALUES (%s, %s, %s, %s)"
            cursor.execute(insert_query, (student_id, subject, score, quiz_date))

            # Retrieve the attendance record for the same student, subject, and quiz_date
            select_query = "SELECT attendance FROM scores WHERE student_id = %s AND subject = %s AND quiz_date = %s"
            cursor.execute(select_query, (student_id, subject, quiz_date))
            attendance_record = cursor.fetchone()

            if attendance_record:
                # If attendance record exists, update attendance only if score is 6 or more
                if score >= 6:
            
                    update_query = "UPDATE scores SET attendance = 'present' WHERE student_id = %s AND subject = %s AND quiz_date = %s"
                    cursor.execute(update_query, (student_id, subject, quiz_date))
            else:
                # If attendance record doesn't exist, insert a new record with appropriate attendance
                    attendance = 'present' if score >= 6 else 'absent'
                    insert_attendance_query = "INSERT INTO scores (student_id, subject, attendance, quiz_date) VALUES (%s, %s, %s, %s)"
                    cursor.execute(insert_attendance_query, (student_id, subject, attendance, quiz_date))

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

    def get_student_quiz_data(self, student_id, subject):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            select_query = "SELECT quiz_date, score FROM scores WHERE student_id = %s AND subject = %s"
            cursor.execute(select_query, (student_id, subject))
            quiz_data = cursor.fetchall()

            return quiz_data

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_student_subjects(self, student_id):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            select_query = "SELECT DISTINCT subject FROM scores WHERE student_id = %s"
            cursor.execute(select_query, (student_id,))
            subjects = [row[0] for row in cursor.fetchall()]

            return subjects

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def get_student_attendance(self, student_id):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            select_query = "SELECT quiz_date, attendance FROM scores WHERE student_id = %s"
            cursor.execute(select_query, (student_id,))
            attendance_records = cursor.fetchall()

            return attendance_records

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_student_scores(self, student_id):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            select_query = "SELECT quiz_date, score FROM scores WHERE student_id = %s"
            cursor.execute(select_query, (student_id,))
            quiz_scores = cursor.fetchall()

            return quiz_scores

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def get_all_subjects(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            select_query = "SELECT DISTINCT subject FROM scores"
            cursor.execute(select_query)
            subjects = [row[0] for row in cursor.fetchall()]

            return subjects

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_all_student_quiz_data(self, subject):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            select_query = "SELECT student_id, score FROM scores WHERE subject = %s"
            cursor.execute(select_query, (subject,))
            quiz_data = cursor.fetchall()

            return quiz_data

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def check_quiz_attempt(self, student_id, subject, quiz_date):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            # Execute a query to check if the combination already exists
            query = "SELECT COUNT(*) FROM scores WHERE student_id = %s AND subject = %s AND quiz_date = %s"
            parameters = (student_id, subject, quiz_date)
            cursor.execute(query, parameters)
            result = cursor.fetchone()

            # If the count is greater than 0, it means the combination already exists
            return result[0] > 0

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False  # Return False in case of an error

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_all_attendance_records(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            select_query = "SELECT student_id, date, subject, marks, attendance FROM attendance_records"
            cursor.execute(select_query)
            attendance_records = cursor.fetchall()

            return attendance_records

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_all_students(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            select_query = "SELECT student_id, student_name FROM students"
            cursor.execute(select_query)
            students = cursor.fetchall()

            return students

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_student_name(self, student_id):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            select_query = "SELECT student_name FROM students WHERE student_id = %s"
            cursor.execute(select_query, (student_id,))
            student_name = cursor.fetchone()[0]

            return student_name

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_student_attendance_records(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            select_query = "SELECT s.student_id, s.student_name, sc.quiz_date, sc.subject, sc.score, sc.attendance FROM students s JOIN scores sc ON s.student_id = sc.student_id"
            cursor.execute(select_query)
            attendance_records = cursor.fetchall()

            return attendance_records

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    def get_all_attendance_records(self):
        try:
            connection = mysql.connector.connect(**self.db_config)
            cursor = connection.cursor()

            select_query = "SELECT student_id, subject, score, quiz_date, attendance FROM scores"
            cursor.execute(select_query)
            attendance_records = cursor.fetchall()

            return attendance_records

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


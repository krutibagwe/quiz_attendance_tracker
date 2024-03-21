'''
import customtkinter as ctk
from welcome_screen import WelcomeScreen  
from attempt_quiz import AttemptQuizSubject

class StudentDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Student Dashboard")

        window_width = 600
        window_height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Student dashboard label
        student_dashboard_label = ctk.CTkLabel(self, text="Student Dashboard", font=("Helvetica", 20))
        student_dashboard_label.pack(pady=20)

        # Buttons
        attempt_quiz_button = ctk.CTkButton(self, text="Attempt Quiz", command=self.attempt_quiz)
        attempt_quiz_button.pack(pady=10)

        view_attendance_button = ctk.CTkButton(self, text="View Attendance", command=self.view_attendance)
        view_attendance_button.pack(pady=10)

        view_past_scores_button = ctk.CTkButton(self, text="View Past Scores", command=self.view_past_scores)
        view_past_scores_button.pack(pady=10)

        #view_study_material_button = ctk.CTkButton(self, text="View Study Material", command=self.view_study_material)
        #view_study_material_button.pack(pady=10)

        logout_button = ctk.CTkButton(self, text="Log Out", command=self.logout)
        logout_button.pack(pady=20)

    def attempt_quiz(self):
        self.withdraw()
        attempt_quiz = AttemptQuizSubject()
        attempt_quiz.mainloop()
        print("Opening Attempt Quiz Window")

    def view_attendance(self):
        print("Opening View Attendance Window")

    def view_past_scores(self):
        print("Opening View Past Scores Window")

    #def view_study_material(self):
       # print("Opening View Study Material Window")

    def logout(self):
        self.withdraw()  
        welcome_screen = WelcomeScreen()
        welcome_screen.mainloop()

if __name__ == "__main__":
    app = StudentDashboard()
    app.mainloop()
'''

import customtkinter as ctk
from welcome_screen import WelcomeScreen  
from attempt_quiz import AttemptQuizSubject
from database_operation import DatabaseOperation
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as tkagg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import tkinter.constants as tk_constants
from tkinter import ttk
import tkinter as tk


# Define the obtain_student_id() function outside the StudentDashboard class
def obtain_student_id():
    from student_login import StudentLogin  # Import the StudentLogin class
    # Create an instance of the StudentLogin class
    login_screen = StudentLogin()

    # Start the login screen's main loop
    login_screen.mainloop()

    # After the main loop finishes (e.g., after successful login), retrieve the student ID
    student_id = login_screen.student_id_var.get()
    print("Student ID Received : ", student_id)
    # Return the obtained student ID
    return student_id
    

class StudentDashboard(ctk.CTk):
    def __init__(self, student_id):
        super().__init__()
        self.title("Student Dashboard")
        self.student_id = student_id
        print("Student ID received in StudentDashboard:", student_id)

        window_width = 600
        window_height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Student dashboard label
        student_dashboard_label = ctk.CTkLabel(self, text="Student Dashboard", font=("Helvetica", 20))
        student_dashboard_label.pack(pady=20)

        # Buttons
        attempt_quiz_button = ctk.CTkButton(self, text="Attempt Quiz", command=self.attempt_quiz)
        attempt_quiz_button.pack(pady=10)

        view_attendance_button = ctk.CTkButton(self, text="View Attendance & Past Scores", command=self.view_details)
        view_attendance_button.pack(pady=10)

        view_progress_button = ctk.CTkButton(self, text="View Progress", command=self.view_details)
        view_progress_button.pack(pady=10)

        #view_study_material_button = ctk.CTkButton(self, text="View Study Material", command=self.view_study_material)
        #view_study_material_button.pack(pady=10)

        logout_button = ctk.CTkButton(self, text="Log Out", command=self.logout)
        logout_button.pack(pady=20)

    def attempt_quiz(self):
        self.withdraw()
        attempt_quiz = AttemptQuizSubject(self.student_id)
        attempt_quiz.mainloop()
        print("Opening Attempt Quiz Window")

    def view_attendance(self):
        print("Opening View Attendance Window")

    def view_details(self):
        db_operation = DatabaseOperation()

        # Fetch data from the database
        attendance_records = db_operation.get_student_attendance(self.student_id)
        quiz_scores = db_operation.get_student_scores(self.student_id)

        # Create a new customtkinter window to display the details
        details_window = ctk.CTk()
        details_window.title("Student Details")

        window_width = 600
        window_height = 400
        details_window.geometry(f"{window_width}x{window_height}")

        screen_width = details_window.winfo_screenwidth()
        screen_height = details_window.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        details_window.geometry(f"+{x_position}+{y_position}")

        # Create a treeview widget
        tree = ttk.Treeview(details_window, columns=("Date", "Marks", "Attendance"), show="headings")
        tree.pack(fill="both", expand=True)

        # Set column headings
        tree.heading("Date", text="Date")
        tree.heading("Marks", text="Marks")
        tree.heading("Attendance", text="Attendance")

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 50))  # Change the font and size as desired


        # Combine the quiz scores and attendance records into a single list
        all_records = []

        # Iterate over both quiz scores and attendance records simultaneously
        quiz_iter = iter(quiz_scores)
        attendance_iter = iter(attendance_records)
        quiz_record = next(quiz_iter, None)
        attendance_record = next(attendance_iter, None)

        while quiz_record or attendance_record:
            # Extract date, marks, and attendance
            date = None
            marks = None
            attendance = None

            if quiz_record:
                date, marks = quiz_record
                quiz_record = next(quiz_iter, None)

            if attendance_record:
                date, attendance = attendance_record
                attendance_record = next(attendance_iter, None)

            # Insert data into the treeview
            tree.insert("", "end", values=(date, marks or "", attendance or ""))

        # Add a button to close the window
        close_button = ctk.CTkButton(details_window, text="Close", command=details_window.withdraw)
        close_button.pack(pady=10)

        details_window.mainloop()

    #def view_study_material(self):
     #   print("Opening View Study Material Window")

    def logout(self):
        self.withdraw()  
        welcome_screen = WelcomeScreen()
        welcome_screen.mainloop()

if __name__ == "__main__":
    from student_login import StudentLogin  # Import the StudentLogin class
    student_id = obtain_student_id()
    app = StudentDashboard(student_id)
    app.mainloop()

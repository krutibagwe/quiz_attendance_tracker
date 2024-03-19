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
        attempt_quiz = AttemptQuizSubject(self.student_id)
        attempt_quiz.mainloop()
        print("Opening Attempt Quiz Window")

    def view_attendance(self):
        print("Opening View Attendance Window")

    def view_past_scores(self):
        print("Opening View Past Scores Window")

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

import customtkinter as ctk
from welcome_screen import WelcomeScreen  # Assuming the file is named welcome_screen.py

class StudentDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Student Dashboard")

        # Set the size of the window and center it
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

        view_study_material_button = ctk.CTkButton(self, text="View Study Material", command=self.view_study_material)
        view_study_material_button.pack(pady=10)

        logout_button = ctk.CTkButton(self, text="Log Out", command=self.logout)
        logout_button.pack(pady=20)

    def attempt_quiz(self):
        # Code to open the Attempt Quiz window goes here
        print("Opening Attempt Quiz Window")

    def view_attendance(self):
        # Code to open the View Attendance window goes here
        print("Opening View Attendance Window")

    def view_past_scores(self):
        # Code to open the View Past Scores window goes here
        print("Opening View Past Scores Window")

    def view_study_material(self):
        # Code to open the View Study Material window goes here
        print("Opening View Study Material Window")

    def logout(self):
        # Code to logout and go back to the Welcome Screen goes here
        self.destroy()  # Close the current window
        welcome_screen = WelcomeScreen()
        welcome_screen.mainloop()

if __name__ == "__main__":
    app = StudentDashboard()
    app.mainloop()

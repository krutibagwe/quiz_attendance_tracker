import customtkinter as ctk
from welcome_screen import WelcomeScreen  # Assuming the file is named welcome_screen.py

class TeacherDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Teacher Dashboard")

        # Set the size of the window and center it
        window_width = 600
        window_height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Teacher dashboard label
        teacher_dashboard_label = ctk.CTkLabel(self, text="Teacher Dashboard", font=("Helvetica", 20))
        teacher_dashboard_label.pack(pady=20)

        # Buttons
        upload_question_button = ctk.CTkButton(self, text="Upload Question", command=self.upload_question)
        upload_question_button.pack(pady=10)

        view_attendance_button = ctk.CTkButton(self, text="View Attendance", command=self.view_attendance)
        view_attendance_button.pack(pady=10)

        view_score_button = ctk.CTkButton(self, text="View Score", command=self.view_score)
        view_score_button.pack(pady=10)

        logout_button = ctk.CTkButton(self, text="Log Out", command=self.logout)
        logout_button.pack(pady=20)

    def upload_question(self):
        # Code to upload quiz goes here
        print("Uploading Question")

    def view_attendance(self):
        # Code to view attendance goes here
        print("Viewing Attendance")

    def view_score(self):
        # Code to view score goes here
        print("Viewing Score")

    def logout(self):
        # Code to logout and go back to the Welcome Screen goes here
        self.destroy()  # Close the current window
        welcome_screen = WelcomeScreen()
        welcome_screen.mainloop()

if __name__ == "__main__":
    app = TeacherDashboard()
    app.mainloop()

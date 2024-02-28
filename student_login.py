import customtkinter as ctk
from database_operation import DatabaseOperation
import tkinter.messagebox as tkmb
from student_dashboard import StudentDashboard

class StudentLogin(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Student Login")

        # Set the size of the window and center it
        window_width = 400
        window_height = 300
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Student Login label
        student_login_label = ctk.CTkLabel(self, text="Student Login", font=("Helvetica", 20))
        student_login_label.pack(pady=20)

        # Student ID and Password entry
        self.student_id_var = ctk.StringVar()
        self.password_var = ctk.StringVar()

        student_id_label = ctk.CTkLabel(self, text="Student ID:")
        student_id_label.pack()
        student_id_entry = ctk.CTkEntry(self, textvariable=self.student_id_var)
        student_id_entry.pack(pady=10)

        password_label = ctk.CTkLabel(self, text="Password:")
        password_label.pack()
        password_entry = ctk.CTkEntry(self, show="*", textvariable=self.password_var)  # Show '*' for password
        password_entry.pack(pady=10)

        # Login button
        login_button = ctk.CTkButton(self, text="Login", command=self.login)
        login_button.pack(pady=20)

    def login(self):
        student_id = self.student_id_var.get()
        password = self.password_var.get()

        # Check if student ID and password match records in the database
        if DatabaseOperation().validate_student_login(student_id, password):
            # Login successful, you can open the student dashboard or perform other actions
            #tkmb.showinfo(title="Login Successful", message="You have logged in successfully")
            self.destroy()
            student_dashboard = StudentDashboard()
            student_dashboard.mainloop()
        else:
            # Login failed, display an error message
            tkmb.showerror(title="Login Failed", message="Incorrect student ID or password. Please try again.")

if __name__ == "__main__":
    app = StudentLogin()
    app.mainloop()

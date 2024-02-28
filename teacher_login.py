import customtkinter as ctk
from database_operation import DatabaseOperation
import tkinter.messagebox as tkmb
from teacher_dashboard import TeacherDashboard

class TeacherLogin(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Teacher Login")

        # Set the size of the window and center it
        window_width = 400
        window_height = 300
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Teacher Login label
        teacher_login_label = ctk.CTkLabel(self, text="Teacher Login", font=("Helvetica", 20))
        teacher_login_label.pack(pady=20)

        # Teacher ID and Password entry
        self.teacher_id_var = ctk.StringVar()
        self.password_var = ctk.StringVar()

        teacher_id_label = ctk.CTkLabel(self, text="Teacher ID:")
        teacher_id_label.pack()
        teacher_id_entry = ctk.CTkEntry(self, textvariable=self.teacher_id_var)
        teacher_id_entry.pack(pady=10)

        password_label = ctk.CTkLabel(self, text="Password:")
        password_label.pack()
        password_entry = ctk.CTkEntry(self, show="*", textvariable=self.password_var)  # Show '*' for password
        password_entry.pack(pady=10)

        # Login button
        login_button = ctk.CTkButton(self, text="Login", command=self.login)
        login_button.pack(pady=20)

    def login(self):
        teacher_id = self.teacher_id_var.get()
        password = self.password_var.get()

        # Check if teacher ID and password match records in the database
        if DatabaseOperation().validate_teacher_login(teacher_id, password):
            # Login successful, you can open the teacher dashboard or perform other actions
            #tkmb.showinfo(title="Login Successful", message="You have logged in successfully")
            self.destroy()
            teacher_dashboard = TeacherDashboard()
            teacher_dashboard.mainloop()
            

        else:
            # Login failed, display an error message
            tkmb.showerror(title="Login Failed", message="Incorrect teacher ID or password. Please try again.")

if __name__ == "__main__":
    app = TeacherLogin()
    app.mainloop()

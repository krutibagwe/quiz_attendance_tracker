import customtkinter as ctk
from welcome_screen import WelcomeScreen 
from add_new_student import AddNewStudent
from add_new_teacher import AddNewTeacher

class AdminDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Admin Dashboard")

        window_width = 600
        window_height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        admin_dashboard_label = ctk.CTkLabel(self, text="Admin Dashboard", font=("Helvetica", 20))
        admin_dashboard_label.pack(pady=20)

        add_student_button = ctk.CTkButton(self, text="Add Student", command=self.open_add_student_window)
        add_student_button.pack(pady=10)

        add_teacher_button = ctk.CTkButton(self, text="Add Teacher", command=self.open_add_teacher_window)
        add_teacher_button.pack(pady=10)

        logout_button = ctk.CTkButton(self, text="Logout", command=self.logout)
        logout_button.pack(pady=20)

    def open_add_student_window(self):
        self.withdraw()
        #print("Opening Add Student Window")
        add_new_student = AddNewStudent()
        add_new_student.mainloop()

    def open_add_teacher_window(self):
        self.withdraw()
        #print("Opening Add Teacher Window")
        add_new_teacher = AddNewTeacher()
        add_new_teacher.mainloop()

    def logout(self):
        self.withdraw()  
        welcome_screen = WelcomeScreen()
        welcome_screen.mainloop()

if __name__ == "__main__":
    app = AdminDashboard()
    app.mainloop()



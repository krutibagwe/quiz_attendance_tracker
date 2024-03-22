import customtkinter as ctk
from database_operation import DatabaseOperation
import tkinter.messagebox as tkmb
from teacher_dashboard import TeacherDashboard

class TeacherLogin(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Teacher Login")

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        window_width = 500
        window_height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        back_button = ctk.CTkButton(self, text="\u2190", command=self.go_back, width=30, height=30)
        back_button.pack(side="top", anchor="nw", padx=10, pady=10)

        teacher_login_label = ctk.CTkLabel(self, text="Teacher Login", font=("Helvetica", 20))
        teacher_login_label.pack(pady=20)

        # Teacher ID and Password entry
        #self.teacher_id_var = ctk.StringVar()
        #self.password_var = ctk.StringVar()

        teacher_id_label = ctk.CTkLabel(self, text="Teacher ID:")
        teacher_id_label.pack()
        self.teacher_id_entry = ctk.CTkEntry(self)
        self.teacher_id_entry.pack(pady=10)

        password_label = ctk.CTkLabel(self, text="Password:")
        password_label.pack()
        self.password_entry = ctk.CTkEntry(self, show="*") 
        self.password_entry.pack(pady=10)

        login_button = ctk.CTkButton(self, text="Login", command=self.login)
        login_button.pack(pady=20)

    def login(self):
        teacher_id = self.teacher_id_entry.get()
        password = self.password_entry.get()

        if DatabaseOperation().validate_teacher_login(teacher_id, password):
            #tkmb.showinfo(title="Login Successful", message="You have logged in successfully")
            self.withdraw()
            teacher_dashboard = TeacherDashboard()
            teacher_dashboard.mainloop()
            

        else:
            tkmb.showerror(title="Login Failed", message="Incorrect teacher ID or password. Please try again.")

    def go_back(self):
        from welcome_screen import WelcomeScreen
        welcome_screen = WelcomeScreen()
        self.withdraw()  
        welcome_screen.mainloop()

if __name__ == "__main__":
    app = TeacherLogin()
    app.mainloop()

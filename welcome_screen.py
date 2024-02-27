import customtkinter as ctk
import tkinter.messagebox as tkmb 
from admin_login import AdminLogin

# Selecting GUI theme - dark, light , system (for system default)
ctk.set_appearance_mode("light")

# Selecting color theme - blue, green, dark-blue
ctk.set_default_color_theme("blue")

class WelcomeScreen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Quiz App")

        # Set the size of the window and center it
        window_width = 600
        window_height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Welcome label
        welcome_label = ctk.CTkLabel(self, text="Welcome to Quiz Connect", font=("Helvetica", 30))
        welcome_label.pack(pady=20)

        ask_label = ctk.CTkLabel(self, text="You are logging in as: ", font=("Helvetica", 15))
        ask_label.pack(pady=10)

        # Buttons
        admin_button = ctk.CTkButton(self, text="Admin", command=self.open_admin_page)
        admin_button.pack(pady=10)

        student_button = ctk.CTkButton(self, text="Student", command=self.open_student_page)
        student_button.pack(pady=10)

        teacher_button = ctk.CTkButton(self, text="Teacher", command=self.open_teacher_page)
        teacher_button.pack(pady=10)

    def open_admin_page(self):
        # Code to open admin page goes here
        #tkmb.showinfo(title="Info",message="Opening Admin Page")
        admin_login = AdminLogin()
        admin_login.mainloop()
        

    def open_student_page(self):
        # Code to open student page goes here
        tkmb.showinfo(title="Info",message="Opening Student Page")

    def open_teacher_page(self):
        # Code to open teacher page goes here
        tkmb.showinfo(title="Info",message="Opening Teacher Page")

if __name__ == "__main__":
    app = WelcomeScreen()
    app.mainloop()

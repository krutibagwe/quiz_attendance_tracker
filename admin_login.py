import customtkinter as ctk
import tkinter.messagebox as tkmb 
from admin_dashboard import AdminDashboard

class AdminLogin(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        self.title("Admin Login")

        window_width = 500
        window_height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        back_button = ctk.CTkButton(self, text="\u2190", command=self.go_back, width=30, height=30)
        back_button.pack(side="top", anchor="nw", padx=10, pady=10)


        # Admin login label
        admin_login_label = ctk.CTkLabel(self, text="Admin Login", font=("Helvetica", 20))
        admin_login_label.pack(pady=20)

        # Admin ID and Password entry
        self.admin_id_var = ctk.StringVar()
        self.password_var = ctk.StringVar()

        admin_id_label = ctk.CTkLabel(self, text="Admin ID:")
        admin_id_label.pack()
        admin_id_entry = ctk.CTkEntry(self, textvariable=self.admin_id_var)
        admin_id_entry.pack(pady=10)

        password_label = ctk.CTkLabel(self, text="Password:")
        password_label.pack()
        password_entry = ctk.CTkEntry(self, textvariable=self.password_var, show="*")
        password_entry.pack(pady=10)

        # Login button
        login_button = ctk.CTkButton(self, text="Login", command=self.check_login)
        login_button.pack(pady=20)

    def check_login(self):
        admin_id = self.admin_id_var.get()
        password = self.password_var.get()

        print(f"admin login {admin_id} password {password}")

        if admin_id == "admin" and password == "12345":
            #tkmb.showinfo("Login Successful", "You have logged in Successfully")
            self.destroy()
            admin_dashboard = AdminDashboard()
            admin_dashboard.mainloop()

        else:
            tkmb.showerror("Error", "Incorrect ID or password. Please try again.")

    def go_back(self):
        from welcome_screen import WelcomeScreen
        welcome_screen = WelcomeScreen()
        self.destroy() 
        welcome_screen.mainloop()



if __name__ == "__main__":
    app = AdminLogin()
    app.mainloop()

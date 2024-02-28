import customtkinter as ctk
from database_operation import DatabaseOperation
import tkinter.messagebox as tkmb

class AddNewTeacher(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Add New Teacher")

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Set the size of the window and center it
        window_width = 400
        window_height = 450
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        back_button = ctk.CTkButton(self, text="\u2190", command=self.go_back, width=30, height=30)
        back_button.pack(side="top", anchor="nw", padx=10, pady=10)

        # Add new teacher label
        add_teacher_label = ctk.CTkLabel(self, text="Add New Teacher", font=("Helvetica", 20))
        add_teacher_label.pack(pady=20)

        # Teacher ID and Password entry
        self.teacher_id_var = ctk.StringVar()
        self.teacher_name_var = ctk.StringVar()
        self.password_var = ctk.StringVar()

        teacher_id_label = ctk.CTkLabel(self, text="Teacher ID:")
        teacher_id_label.pack()
        teacher_id_entry = ctk.CTkEntry(self, textvariable=self.teacher_id_var)
        teacher_id_entry.pack(pady=10)

        teacher_name_label = ctk.CTkLabel(self, text="Teacher Name:")
        teacher_name_label.pack()
        teacher_name_entry = ctk.CTkEntry(self, textvariable=self.teacher_name_var)
        teacher_name_entry.pack(pady=10)

        password_label = ctk.CTkLabel(self, text="Password:")
        password_label.pack()
        password_entry = ctk.CTkEntry(self, textvariable=self.password_var)
        password_entry.pack(pady=10)

        # Create Teacher button
        create_teacher_button = ctk.CTkButton(self, text="Create Teacher", command=self.create_teacher)
        create_teacher_button.pack(pady=20)

    def create_teacher(self):
        teacher_id = self.teacher_id_var.get()
        teacher_name = self.teacher_name_var.get()
        password = self.password_var.get()

        # Code to store teacher_id, teacher_name, and password in the database goes here
        DatabaseOperation().add_teacher(teacher_id, teacher_name, password)
        # Optionally, show a message indicating success
        tkmb.showinfo(title="Success", message="Teacher created successfully")
        self.destroy()

    def go_back(self):
        from admin_dashboard import AdminDashboard
        admin_dashboard = AdminDashboard()
        self.destroy()  # Close the StudentLogin window
        admin_dashboard.mainloop()

if __name__ == "__main__":
    app = AddNewTeacher()
    app.mainloop()

import customtkinter as ctk
from database_operation import DatabaseOperation
import tkinter.messagebox as tkmb

class AddNewTeacher(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Add New Teacher")

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

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
        self.teacher_id_label = ctk.CTkLabel(self, text="Teacher ID:")
        self.teacher_id_label.pack()
        self.teacher_id_entry = ctk.CTkEntry(self)
        self.teacher_id_entry.pack(pady=10)

        self.teacher_name_label = ctk.CTkLabel(self, text="Teacher Name:")
        self.teacher_name_label.pack()
        self.teacher_name_entry = ctk.CTkEntry(self)
        self.teacher_name_entry.pack(pady=10)

        self.password_label = ctk.CTkLabel(self, text="Password:")
        self.password_label.pack()
        self.password_entry = ctk.CTkEntry(self)
        self.password_entry.pack(pady=10)

        # Create Teacher button
        create_teacher_button = ctk.CTkButton(self, text="Create Teacher", command=self.create_teacher)
        create_teacher_button.pack(pady=20)

    def create_teacher(self):
        teacher_id = self.teacher_id_entry.get()
        teacher_name = self.teacher_name_entry.get()
        password = self.password_entry.get()

        DatabaseOperation().add_teacher(teacher_id, teacher_name, password)
        tkmb.showinfo(title="Success", message="Teacher created successfully")
        self.withdraw()
        from admin_dashboard import AdminDashboard
        admin_dashboard = AdminDashboard()
        admin_dashboard.mainloop()

    def go_back(self):
        from admin_dashboard import AdminDashboard
        admin_dashboard = AdminDashboard()
        self.withdraw()  
        admin_dashboard.mainloop()

if __name__ == "__main__":
    app = AddNewTeacher()
    app.mainloop()

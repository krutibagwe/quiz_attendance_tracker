import customtkinter as ctk
from database_operation import DatabaseOperation
import tkinter.messagebox as tkmb

class AddNewStudent(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Add New Student")

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


        # Add new student label
        add_student_label = ctk.CTkLabel(self, text="Add New Student", font=("Helvetica", 20))
        add_student_label.pack(pady=20)

        # Student ID and Password entry
        self.student_id_var = ctk.StringVar()
        self.student_name_var = ctk.StringVar()
        self.student_department_var = ctk.StringVar()
        self.student_year_var = ctk.StringVar()
        self.student_password_var = ctk.StringVar()

        student_id_label = ctk.CTkLabel(self, text="Student ID:")
        student_id_label.pack()
        student_id_entry = ctk.CTkEntry(self, textvariable=self.student_id_var)
        student_id_entry.pack(pady=10)

        student_name_label = ctk.CTkLabel(self, text="Student Name:")  
        student_name_label.pack()
        student_name_entry = ctk.CTkEntry(self, textvariable=self.student_name_var)
        student_name_entry.pack(pady=10)

        student_department_label = ctk.CTkLabel(self, text="Student Department:")  
        student_department_label.pack()
        student_department_entry = ctk.CTkEntry(self, textvariable=self.student_department_var)
        student_department_entry.pack(pady=10)

        student_year_label = ctk.CTkLabel(self, text="Student Year:")  
        student_year_label.pack()
        student_year_entry = ctk.CTkEntry(self, textvariable=self.student_year_var)
        student_year_entry.pack(pady=10)


        student_password_label = ctk.CTkLabel(self, text="Password:")
        student_password_label.pack()
        student_password_entry = ctk.CTkEntry(self, textvariable=self.student_password_var)
        student_password_entry.pack(pady=10)

        # Create Student button
        create_student_button = ctk.CTkButton(self, text="Create Student", command=self.create_student)
        create_student_button.pack(pady=20)

    def create_student(self):
        student_id = self.student_id_var.get()
        student_name = self.student_name_var.get()  
        student_department = self.student_department_var.get()
        student_year = self.student_year_var.get()
        student_password = self.student_password_var.get()

        DatabaseOperation().add_student(student_id, student_name, student_department, student_year, student_password)

        print(f"Values: {student_id}, {student_name}, {student_department}, {student_year}, {student_password}")

        tkmb.showinfo(title="Success",message="Student created successfully")
        self.destroy()

    def go_back(self):
        from admin_dashboard import AdminDashboard
        admin_dashboard = AdminDashboard()
        self.destroy()  
        admin_dashboard.mainloop()
    

if __name__ == "__main__":
    app = AddNewStudent()
    app.mainloop()

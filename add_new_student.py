import customtkinter as ctk
from database_operation import DatabaseOperation
import tkinter.messagebox as tkmb

class AddNewStudent(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Add New Student")

        # Set the size of the window and center it
        window_width = 400
        window_height = 450
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Add new student label
        add_student_label = ctk.CTkLabel(self, text="Add New Student", font=("Helvetica", 20))
        add_student_label.pack(pady=20)

        # Student ID and Password entry
        self.student_id_var = ctk.StringVar()
        self.student_name_var = ctk.StringVar()
        self.password_var = ctk.StringVar()

        student_id_label = ctk.CTkLabel(self, text="Student ID:")
        student_id_label.pack()
        student_id_entry = ctk.CTkEntry(self, textvariable=self.student_id_var)
        student_id_entry.pack(pady=10)

        student_name_label = ctk.CTkLabel(self, text="Student Name:")  
        student_name_label.pack()
        student_name_entry = ctk.CTkEntry(self, textvariable=self.student_name_var)
        student_name_entry.pack(pady=10)


        password_label = ctk.CTkLabel(self, text="Password:")
        password_label.pack()
        password_entry = ctk.CTkEntry(self, textvariable=self.password_var)
        password_entry.pack(pady=10)

        # Create Student button
        create_student_button = ctk.CTkButton(self, text="Create Student", command=self.create_student)
        create_student_button.pack(pady=20)

    def create_student(self):
        student_id = self.student_id_var.get()
        student_name = self.student_name_var.get()  # Add an entry for student name
        password = self.password_var.get()

    # Code to store student_id, student_name, and password in the database goes here
        DatabaseOperation().add_student(student_id, student_name, password)
        # Optionally, show a message indicating success
        tkmb.showinfo(title="Success",message="Student created successfully")

if __name__ == "__main__":
    app = AddNewStudent()
    app.mainloop()

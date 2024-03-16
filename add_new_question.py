'''
import customtkinter as ctk
from database_operation import DatabaseOperation
import tkinter.messagebox as tkmb


class AddNewQuestion(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Add New Question")

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        window_width = 600
        window_height = 725
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

          # Back button
        back_button = ctk.CTkButton(self, text="\u2190", command=self.go_back, width=30, height=30)
        back_button.pack(side="top", anchor="nw", padx=10, pady=10)

        # Add new question label
        add_question_label = ctk.CTkLabel(self, text="Add New Question", font=("Helvetica", 20))
        add_question_label.pack(pady=20)


        subject_label = ctk.CTkLabel(self, text="Select Subject:")
        subject_label.pack()
        subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]

        self.subject_var = ctk.StringVar(value=subjects[0])  

        def subject_dropdown_callback(choice):
            self.subject_var.set(choice)

        subject_dropdown = ctk.CTkOptionMenu(self, values=subjects, command=subject_dropdown_callback, variable=self.subject_var)
        
        subject_dropdown.pack(pady=10)

        # Question, Options, and Correct Option entry
        question_label = ctk.CTkLabel(self, text="Enter Question:")
        question_label.pack()
        self.question_text_var = ctk.StringVar()
        question_entry = ctk.CTkEntry(self, textvariable=self.question_text_var)
        question_entry.pack(pady=10)

        options_label = ctk.CTkLabel(self, text="Enter Options:")
        options_label.pack()

        option_a_label = ctk.CTkLabel(self, text="Option A:")
        option_a_label.pack()
        self.option_a_var = ctk.StringVar()
        option_a_entry = ctk.CTkEntry(self, textvariable=self.option_a_var)
        option_a_entry.pack(pady=5)

        option_b_label = ctk.CTkLabel(self, text="Option B:")
        option_b_label.pack()
        self.option_b_var = ctk.StringVar()
        option_b_entry = ctk.CTkEntry(self, textvariable=self.option_b_var)
        option_b_entry.pack(pady=5)

        option_c_label = ctk.CTkLabel(self, text="Option C:")
        option_c_label.pack()
        self.option_c_var = ctk.StringVar()
        option_c_entry = ctk.CTkEntry(self, textvariable=self.option_c_var)
        option_c_entry.pack(pady=5)

        option_d_label = ctk.CTkLabel(self, text="Option D:")
        option_d_label.pack()
        self.option_d_var = ctk.StringVar()
        option_d_entry = ctk.CTkEntry(self, textvariable=self.option_d_var)
        option_d_entry.pack(pady=5)

        correct_option_label = ctk.CTkLabel(self, text="Enter Correct Option (A/B/C/D):")
        correct_option_label.pack()
        self.correct_option_var = ctk.StringVar()
        correct_option_entry = ctk.CTkEntry(self, textvariable=self.correct_option_var)
        correct_option_entry.pack(pady=10)

        # Add Question button
        add_question_button = ctk.CTkButton(self, text="Add Question", command=self.add_question)
        add_question_button.pack(pady=20)

    def add_question(self):
        subject = self.subject_var.get()
        question_text = self.question_text_var.get()
        option_a = self.option_a_var.get()
        option_b = self.option_b_var.get()
        option_c = self.option_c_var.get()
        option_d = self.option_d_var.get()
        correct_option = self.correct_option_var.get()

        DatabaseOperation().add_question(subject, question_text, option_a, option_b, option_c, option_d, correct_option)
        tkmb.showinfo(title="Success", message="Question added successfully")
        self.destroy()

    def go_back(self):
        from student_dashboard import StudentDashboard
        student_dashboard = StudentDashboard()
        self.destroy() 
        student_dashboard.mainloop()

if __name__ == "__main__":
    app = AddNewQuestion()
    app.mainloop()
'''

    
import customtkinter as ctk
from database_operation import DatabaseOperation
import tkinter.messagebox as tkmb

class AddNewQuestion(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Add New Question")

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        window_width = 600
        window_height = 725
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        back_button = ctk.CTkButton(self, text="\u2190", command=self.go_back, width=30, height=30)
        back_button.pack(side="top", anchor="nw", padx=10, pady=10)

        add_question_label = ctk.CTkLabel(self, text="Add New Question", font=("Helvetica", 20))
        add_question_label.pack(pady=1)


        subject_label = ctk.CTkLabel(self, text="Select Subject:")
        subject_label.pack()
        subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]

        self.subject = subjects[0]

        def subject_dropdown_callback(choice):
            self.subject = choice

        subject_dropdown = ctk.CTkOptionMenu(self, values=subjects, command=subject_dropdown_callback)
        subject_dropdown.pack(pady=10)

        question_label = ctk.CTkLabel(self, text="Enter Question:")
        question_label.pack()
        question_entry = ctk.CTkEntry(self)
        question_entry.pack(pady=10)

        options_label = ctk.CTkLabel(self, text="Enter Options:")
        options_label.pack()

        option_a_label = ctk.CTkLabel(self, text="Option A:")
        option_a_label.pack()
        option_a_entry = ctk.CTkEntry(self)
        option_a_entry.pack(pady=5)

        option_b_label = ctk.CTkLabel(self, text="Option B:")
        option_b_label.pack()
        option_b_entry = ctk.CTkEntry(self)
        option_b_entry.pack(pady=5)

        option_c_label = ctk.CTkLabel(self, text="Option C:")
        option_c_label.pack()
        option_c_entry = ctk.CTkEntry(self)
        option_c_entry.pack(pady=5)

        option_d_label = ctk.CTkLabel(self, text="Option D:")
        option_d_label.pack()
        option_d_entry = ctk.CTkEntry(self)
        option_d_entry.pack(pady=5)

        correct_option_label = ctk.CTkLabel(self, text="Enter Correct Option (A/B/C/D):")
        correct_option_label.pack()
        correct_option_entry = ctk.CTkEntry(self)
        correct_option_entry.pack(pady=10)

        add_question_button = ctk.CTkButton(self, text="Add Question", command=lambda: self.add_question(question_entry.get(), option_a_entry.get(), option_b_entry.get(), option_c_entry.get(), option_d_entry.get(), correct_option_entry.get()))
        add_question_button.pack(pady=20)

    def add_question(self, question_text, option_a, option_b, option_c, option_d, correct_option):
        DatabaseOperation().add_question(self.subject, question_text, option_a, option_b, option_c, option_d, correct_option)
        tkmb.showinfo(title="Success", message="Question added successfully")
        self.destroy()

    def go_back(self):
        from student_dashboard import StudentDashboard
        student_dashboard = StudentDashboard()
        self.destroy() 
        student_dashboard.mainloop()

if __name__ == "__main__":
    app = AddNewQuestion()
    app.mainloop()



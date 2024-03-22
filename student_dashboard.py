import customtkinter as ctk
from welcome_screen import WelcomeScreen  
from attempt_quiz import AttemptQuizSubject
from database_operation import DatabaseOperation
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as tkagg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import tkinter.constants as tk_constants
from tkinter import ttk
import tkinter as tk


def obtain_student_id():
    from student_login import StudentLogin 

    login_screen = StudentLogin()

    login_screen.mainloop()

    #  retrieve the student ID
    student_id = login_screen.student_id_var.get()
    print("Student ID Received : ", student_id)

    return student_id
    

class StudentDashboard(ctk.CTk):
    def __init__(self, student_id):
        super().__init__()
        self.title("Student Dashboard")
        self.student_id = student_id
        print("Student ID received in StudentDashboard:", student_id)

        window_width = 600
        window_height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Student dashboard label
        student_dashboard_label = ctk.CTkLabel(self, text="Student Dashboard", font=("Helvetica", 20))
        student_dashboard_label.pack(pady=20)

        # Buttons
        attempt_quiz_button = ctk.CTkButton(self, text="Attempt Quiz", command=self.attempt_quiz)
        attempt_quiz_button.pack(pady=10)

        view_attendance_button = ctk.CTkButton(self, text="Attendance & Score", command=self.view_details)
        view_attendance_button.pack(pady=10)

        view_progress_button = ctk.CTkButton(self, text="Progress ", command=self.view_progress)
        view_progress_button.pack(pady=10)

        #view_study_material_button = ctk.CTkButton(self, text="View Study Material", command=self.view_study_material)
        #view_study_material_button.pack(pady=10)

        logout_button = ctk.CTkButton(self, text="Log Out", command=self.logout)
        logout_button.pack(pady=20)

    def attempt_quiz(self):
        self.withdraw()
        attempt_quiz = AttemptQuizSubject(self.student_id)
        attempt_quiz.mainloop()
        print("Opening Attempt Quiz Window")

    def view_details(self):
        self.withdraw()
        db_operation = DatabaseOperation()

        attendance_records = db_operation.get_student_attendance(self.student_id)
        quiz_scores = db_operation.get_student_scores(self.student_id)

        details_window = ctk.CTk()
        details_window.title("Student Details")

        window_width = 600
        window_height = 400
        details_window.geometry(f"{window_width}x{window_height}")

        screen_width = details_window.winfo_screenwidth()
        screen_height = details_window.winfo_screenheight()
        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2
        details_window.geometry(f"+{x_position}+{y_position}")

        # Create a treeview widget
        tree = ttk.Treeview(details_window, columns=("Date", "Marks", "Attendance"), show="headings")
        tree.pack(fill="both", expand=True)

        tree.heading("Date", text="Date", anchor = "center")
        tree.heading("Marks", text="Marks", anchor = "center")
        tree.heading("Attendance", text="Attendance", anchor = "center")

        for col in tree["columns"]:
            tree.column(col, anchor="center")

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 50))  


        # Combine the quiz scores and attendance records into a single list
        all_records = []

        # Iterate over both quiz scores and attendance records simultaneously
        quiz_iter = iter(quiz_scores)
        attendance_iter = iter(attendance_records)
        quiz_record = next(quiz_iter, None)
        attendance_record = next(attendance_iter, None)

        while quiz_record or attendance_record:
            # Extract date, marks, and attendance
            date = None
            marks = None
            attendance = None

            if quiz_record:
                date, marks = quiz_record
                quiz_record = next(quiz_iter, None)

            if attendance_record:
                date, attendance = attendance_record
                attendance_record = next(attendance_iter, None)

            tree.insert("", "end", values=(date, marks or "", attendance or ""))      

        def close_window():
                details_window.withdraw()
                from teacher_dashboard import TeacherDashboard
                teacher_dashboard = TeacherDashboard()
                teacher_dashboard.mainloop()
           
        close_button = ctk.CTkButton(details_window, text="Close", command=close_window)
        close_button.pack(pady=10)

        details_window.mainloop()

    def view_progress(self):
        db_operation = DatabaseOperation()
        subjects = db_operation.get_student_subjects(self.student_id)

        root = ctk.CTk()
        root.title("Progress for All Subjects")

        # Define grid layout parameters
        rows = 2
        cols = 3

        for i, subject in enumerate(subjects):
            quiz_data = db_operation.get_student_quiz_data(self.student_id, subject)
            
            if quiz_data:
                quiz_dates = [data[0] for data in quiz_data]
                scores = [data[1] for data in quiz_data]
                
                fig, ax = plt.subplots(figsize=(5, 5))
                ax.plot(quiz_dates, scores, marker='o')
                ax.set_title(f'Progress in {subject}')
                ax.set_xlabel('Date of Quiz')
                ax.set_ylabel('Marks Obtained')
                ax.grid(True)
                #ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better visibility

                # Embed the plot into a tkinter window
                canvas = tkagg.FigureCanvasTkAgg(fig, master=root)
                canvas.draw()
                
                row = i // cols
                col = i % cols
                
                canvas.get_tk_widget().grid(row=row, column=col, padx=10, pady=10)
                
            else:
                print(f"No quiz data found for {subject}")

        close_button = ctk.CTkButton(root, text="Close", command=root.withdraw)
        close_button.grid(row=rows, column=0, columnspan=cols, pady=10)

        root.mainloop()

      

    def logout(self):
        self.withdraw()  
        welcome_screen = WelcomeScreen()
        welcome_screen.mainloop()

if __name__ == "__main__":
    from student_login import StudentLogin  
    student_id = obtain_student_id()
    app = StudentDashboard(student_id)
    app.mainloop()

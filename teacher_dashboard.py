from welcome_screen import WelcomeScreen  
from add_new_question import AddNewQuestion
import customtkinter as ctk
import matplotlib.backends.backend_tkagg as tkagg
import matplotlib.pyplot as plt
from database_operation import DatabaseOperation
from tkinter import ttk


class TeacherDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Teacher Dashboard")

        window_width = 600
        window_height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        teacher_dashboard_label = ctk.CTkLabel(self, text="Teacher Dashboard", font=("Helvetica", 20))
        teacher_dashboard_label.pack(pady=20)

        upload_question_button = ctk.CTkButton(self, text="Upload Question", command=self.upload_question)
        upload_question_button.pack(pady=10)

        view_attendance_button = ctk.CTkButton(self, text="Attendance & Scores", command=self.view_attendance)
        view_attendance_button.pack(pady=10)

        view_student_progress_button = ctk.CTkButton(self, text="Student Progress", command=self.view_student_progress)
        view_student_progress_button.pack(pady=10)

        logout_button = ctk.CTkButton(self, text="Log Out", command=self.logout)
        logout_button.pack(pady=20)

    def upload_question(self):
        #print("Uploading Question")
        self.withdraw()
        add_new_question = AddNewQuestion()
        add_new_question.mainloop()


    def view_attendance(self):
        self.withdraw()
        db_operation = DatabaseOperation()

        # Fetch attendance records from the database
        attendance_records = db_operation.get_all_attendance_records()

        if attendance_records:
            attendance_window = ctk.CTk()
            attendance_window.title("Attendance Records")

            window_width = 600
            window_height = 400
            attendance_window.geometry(f"{window_width}x{window_height}")

            screen_width = attendance_window.winfo_screenwidth()
            screen_height = attendance_window.winfo_screenheight()
            x_position = (screen_width - window_width) // 2
            y_position = (screen_height - window_height) // 2
            attendance_window.geometry(f"+{x_position}+{y_position}")

            # Create a treeview widget
            tree = ttk.Treeview(attendance_window, columns=("Student ID", "Subject", "Score","Date", "Attendance"), show="headings")
            tree.pack(fill="both", expand=True)

            tree.heading("Student ID", text="Student ID", anchor = "center")
            tree.heading("Subject", text="Subject", anchor = "center")
            tree.heading("Score", text="Score", anchor = "center")
            tree.heading("Date", text="Date", anchor = "center")
            tree.heading("Attendance", text="Attendance", anchor = "center")

            tree.column("Student ID", width=100)
            tree.column("Subject", width=100)
            tree.column("Score", width=50)
            tree.column("Date", width=100)
            tree.column("Attendance", width=100)

            for col in tree["columns"]:
                tree.column(col, anchor="center")

            # Insert data into the treeview
            for idx, record in enumerate(attendance_records, start=1):
                tree.insert("", "end", values=(record[0], record[1], record[2], record[3], record[4]))
            
            def close_window():
                attendance_window.withdraw()
                from teacher_dashboard import TeacherDashboard
                teacher_dashboard = TeacherDashboard()
                teacher_dashboard.mainloop()
           
            close_button = ctk.CTkButton(attendance_window, text="Close", command=close_window)
            close_button.pack(pady=10)

            attendance_window.mainloop()
        else:
            print("No attendance records found.")

        

    def view_student_progress(self):
        db_operation = DatabaseOperation()
        subjects = db_operation.get_all_subjects()  

        root = ctk.CTk()
        root.title("Progress for All Subjects")

        # Define grid layout parameters
        rows = 2
        cols = 3

        for i, subject in enumerate(subjects):
            # Get quiz data for the subject
            quiz_data = db_operation.get_all_student_quiz_data(subject)
            
            if quiz_data:
                student_ids = [data[0] for data in quiz_data]
                marks = [data[1] for data in quiz_data]

                fig, ax = plt.subplots(figsize=(5, 5))
                ax.scatter(student_ids, marks, marker='o', linestyle='-')
                ax.set_title(f'Progress in {subject}')
                ax.set_xlabel('Student ID')
                ax.set_ylabel('Marks Obtained')
                ax.grid(True)

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
    app = TeacherDashboard()
    app.mainloop()

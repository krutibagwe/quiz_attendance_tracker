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

        # Teacher dashboard label
        teacher_dashboard_label = ctk.CTkLabel(self, text="Teacher Dashboard", font=("Helvetica", 20))
        teacher_dashboard_label.pack(pady=20)

        # Buttons
        upload_question_button = ctk.CTkButton(self, text="Upload Question", command=self.upload_question)
        upload_question_button.pack(pady=10)

        view_attendance_button = ctk.CTkButton(self, text="View Attendance", command=self.view_attendance)
        view_attendance_button.pack(pady=10)

        view_student_progress_button = ctk.CTkButton(self, text="View Progress", command=self.view_student_progress)
        view_student_progress_button.pack(pady=10)

        logout_button = ctk.CTkButton(self, text="Log Out", command=self.logout)
        logout_button.pack(pady=20)

    def upload_question(self):
        #print("Uploading Question")
        self.withdraw()
        add_new_question = AddNewQuestion()
        add_new_question.mainloop()


    def view_attendance(self):
        db_operation = DatabaseOperation()

        # Fetch attendance records from the database
        attendance_records = db_operation.get_all_attendance_records()

        if attendance_records:
            # Create a new customtkinter window to display the attendance table
            attendance_window = ctk.CTk()
            attendance_window.title("Attendance Records")

            window_width = 800
            window_height = 600
            screen_width = attendance_window.winfo_screenwidth()
            screen_height = attendance_window.winfo_screenheight()

            x_position = (screen_width - window_width) // 2
            y_position = (screen_height - window_height) // 2

            attendance_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

            # Create a treeview widget
            tree = ttk.Treeview(attendance_window, columns=("Student ID", "Subject", "Score","Date", "Attendance"), show="headings")
            tree.pack(fill="both", expand=True)

            # Set column headings
            tree.heading("Student ID", text="Student ID")
            tree.heading("Subject", text="Subject")
            tree.heading("Score", text="Score")
            tree.heading("Date", text="Date")
            tree.heading("Attendance", text="Attendance")

            # Insert data into the treeview
            for idx, record in enumerate(attendance_records, start=1):
                tree.insert("", "end", values=(record[0], record[1], record[2], record[3], record[4]))
            
            close_button = ctk.CTkButton(attendance_window, text="Close", command=attendance_window.withdraw)
            close_button.pack(pady=10)

            attendance_window.mainloop()
        else:
            print("No attendance records found.")

        


    def view_student_progress(self):
        db_operation = DatabaseOperation()
        subjects = db_operation.get_all_subjects()  # Get all subjects

        # Create a tkinter window
        root = ctk.CTk()
        root.title("Progress for All Subjects")

        # Define grid layout parameters
        rows = 2
        cols = 3

        for i, subject in enumerate(subjects):
            # Get quiz data for the subject
            quiz_data = db_operation.get_all_student_quiz_data(subject)
            
            if quiz_data:
                # Extract student IDs and corresponding marks
                student_ids = [data[0] for data in quiz_data]
                marks = [data[1] for data in quiz_data]
                
                # Create a subplot for the subject
                fig, ax = plt.subplots(figsize=(5, 5))
                ax.scatter(student_ids, marks, marker='o', linestyle='-')
                ax.set_title(f'Progress in {subject}')
                ax.set_xlabel('Student ID')
                ax.set_ylabel('Marks Obtained')
                ax.grid(True)

                # Embed the plot into a tkinter window
                canvas = tkagg.FigureCanvasTkAgg(fig, master=root)
                canvas.draw()
                
                # Calculate grid coordinates for the current subplot
                row = i // cols
                col = i % cols
                
                # Pack the canvas into the appropriate grid cell
                canvas.get_tk_widget().grid(row=row, column=col, padx=10, pady=10)
                
            else:
                print(f"No quiz data found for {subject}")

        # Add a button to close the window
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

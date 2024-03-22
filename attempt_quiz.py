import customtkinter as ctk
from database_operation import DatabaseOperation 
import tkinter as tk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg as tkagg
import tkinter.messagebox as tkmb


def obtain_student_id():
    from student_login import StudentLogin
    login_screen = StudentLogin()

    login_screen.mainloop()

    #retrieve the student ID
    student_id = login_screen.student_id_var.get()
    print("Student ID :" , student_id)

    # Return the obtained student ID
    return student_id

class AttemptQuizSubject(ctk.CTk):
    def __init__(self, student_id):
        super().__init__()
        self.student_id = student_id

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.title("Attempt Quiz - Select Subject")

        window_width = 700
        window_height = 565
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        back_button = ctk.CTkButton(self, text="\u2190", command=self.go_back, width=30, height=30)
        back_button.pack(side="top", anchor="nw", padx=10, pady=10)

        select_subject_label = ctk.CTkLabel(self, text="Select Subject", font=("Helvetica", 20))
        select_subject_label.pack(pady=20)

        subjects = ["DSA", "DBMS","Engg Maths-3", "PCOM", "PCPF" ]
        self.subject_var = ctk.StringVar(value=subjects[0])

        def subject_dropdown_callback(choice):
            self.subject_var.set(choice)

        subject_dropdown = ctk.CTkOptionMenu(self, values=subjects, command=subject_dropdown_callback, variable=self.subject_var)
        subject_dropdown.pack(pady=10)

        self.date_label = ctk.CTkLabel(self, text="Enter Date: (DD/MM/YY)", font=("Helvetica", 12))
        self.date_label.pack(pady=10)
        self.date_entry = ctk.CTkEntry(self)
        self.date_entry.pack(pady=5)


        instructions_label = ctk.CTkLabel(self, text="Read the instructions below before starting the quiz:", font=("Helvetica", 15))
        instructions_label.pack(pady=5)

        instructions_text = """
        1. This quiz consists of 10 multiple-choice questions.
        2. Select the correct answer for each question.
        3. You cannot go back to previous questions, so answer carefully.
        4. You must attempt all questions.
        5. Attendance will be marked as present if score is 6 or more.
        4. Click the 'Start Quiz' button when you are ready.
        """

        instructions_text_label = ctk.CTkLabel(self, text=instructions_text, font=("Helvetica", 15), justify=ctk.LEFT, wraplength=500)
        instructions_text_label.pack(pady=30)

        start_quiz_button = ctk.CTkButton(self, text="Start Quiz", command=self.start_quiz)
        start_quiz_button.pack(pady=20)

    def start_quiz(self):
        selected_subject = self.subject_var.get()

        questions = DatabaseOperation().get_quiz_questions(selected_subject)
        print("Questions:", questions)

        quiz_date = self.date_entry.get()

        if DatabaseOperation().check_quiz_attempt(self.student_id, selected_subject, quiz_date):
            # Display a message that the user has already responded
            tkmb.showinfo("Quiz Attempted", "You have already responded to this quiz.")
            self.withdraw()
            from student_dashboard import StudentDashboard
            student_dashboard = StudentDashboard(self.student_id)
            student_dashboard.mainloop()
        
           
        else:
            print(f"Student ID before starting quiz: {self.student_id}")



            print(f"Student ID before starting quiz: {self.student_id}")
            
            self.withdraw()
            
            quiz_window = QuizWindow(self.student_id, selected_subject, questions, quiz_date)
            quiz_window.mainloop()

    def go_back(self):
        from student_dashboard import StudentDashboard  
        student_dashboard = StudentDashboard(self.student_id)  
        self.withdraw()
        student_dashboard.mainloop()

class QuizWindow(ctk.CTk):
    def __init__(self, student_id, selected_subject, questions, quiz_date):
        super().__init__()

        self.title("Quiz")
        self.student_id = student_id
        self.selected_subject = selected_subject
        self.questions = DatabaseOperation().get_quiz_questions(selected_subject)
        self.quiz_date = quiz_date

        self.current_question_index = 0
        self.correct_answers = 0

        window_width = 600
        window_height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.create_widgets()

    def create_widgets(self):
        self.question_label = ctk.CTkLabel(self, text="", font=("Helvetica", 14))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        options = ["A", "B", "C", "D"]
        for option in options:
            button = ctk.CTkButton(self, text="", command=lambda o=option: self.answer_question(o))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.update_question()

    def update_question(self):
        if self.current_question_index < len(self.questions):
            question_text, option_a, option_b, option_c, option_d, correct_option = self.questions[self.current_question_index]
            self.question_label.configure(text=question_text)

            options = [option_a, option_b, option_c, option_d]
            for i, option in enumerate(options):
                self.option_buttons[i].configure(text=f"{chr(65 + i)}. {option}")

        else:
            self.show_result()

    def answer_question(self, selected_option):
        correct_option = self.questions[self.current_question_index][-1]

        if selected_option == correct_option:
            self.correct_answers += 1

        self.current_question_index += 1
        self.update_question()

    def show_result(self):
        # Clear the window
        for widget in self.winfo_children():
            widget.destroy()
        
        score_frame = ctk.CTkFrame(self)
        score_frame.pack(expand=True)

        # Display the score
        score_text = f"Quiz completed!\nYou scored {self.correct_answers}/{len(self.questions)}"
        score_label = ctk.CTkLabel(score_frame, text=score_text, font=("Helvetica", 14))
        score_label.pack(pady=10)

        database = DatabaseOperation()
        database.add_score(self.student_id, self.selected_subject, self.correct_answers, self.quiz_date)

        back_button_frame = ctk.CTkFrame(self)
        back_button_frame.pack(side="top", anchor="nw", padx=10, pady=10)

        back_button = ctk.CTkButton(back_button_frame, text="\u2190", command=self.go_back, width=30, height=30)
        back_button.pack(side="left")

        # Display the pie chart
        self.display_pie_chart()

    def go_back(self):
        from student_dashboard import StudentDashboard
        student_dashboard = StudentDashboard(self.student_id)
        self.withdraw()
        student_dashboard.mainloop()

    def display_pie_chart(self):
        correct_count = self.correct_answers
        incorrect_count = len(self.questions) - self.correct_answers

        fig, ax = plt.subplots(figsize=(4, 4))
        ax.pie([correct_count, incorrect_count], labels=["Correct", "Incorrect"], autopct='%1.1f%%', startangle=140)
        ax.set_title(f'Quiz Performance for {self.selected_subject}')

        canvas = tkagg.FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    student_id = obtain_student_id()  
    app = AttemptQuizSubject(student_id)
    app.mainloop()
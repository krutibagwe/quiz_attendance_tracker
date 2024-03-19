'''
import customtkinter as ctk
from database_operation import DatabaseOperation 

class AttemptQuizSubject(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.title("Attempt Quiz - Select Subject")

        window_width = 600
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        back_button = ctk.CTkButton(self, text="\u2190", command=self.go_back, width=30, height=30)
        back_button.pack(side="top", anchor="nw", padx=10, pady=10)

        select_subject_label = ctk.CTkLabel(self, text="Select Subject", font=("Helvetica", 20))
        select_subject_label.pack(pady=20)

        subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
        self.subject_var = ctk.StringVar(value=subjects[0])

        def subject_dropdown_callback(choice):
            self.subject_var.set(choice)

        subject_dropdown = ctk.CTkOptionMenu(self, values=subjects, command=subject_dropdown_callback, variable=self.subject_var)
        subject_dropdown.pack(pady=10)

        instructions_label = ctk.CTkLabel(self, text="Read the instructions below before starting the quiz:", font=("Helvetica", 15))
        instructions_label.pack(pady=10)

        instructions_text = """
        1. This quiz consists of multiple-choice questions.
        2. Select the correct answer for each question.
        3. You cannot go back to previous questions, so answer carefully.
        4. Click the 'Start Quiz' button when you are ready.
        """

        instructions_text_label = ctk.CTkLabel(self, text=instructions_text, font=("Helvetica", 15), justify=ctk.LEFT, wraplength=500)
        instructions_text_label.pack(pady=20)


        start_quiz_button = ctk.CTkButton(self, text="Start Quiz", command=self.start_quiz)
        start_quiz_button.pack(pady=20)

    def start_quiz(self):
        # Get the selected subject
        selected_subject = self.subject_var.get()
        
        # Close the subject selection window
        self.withdraw()
        
        # Open the quiz window for the selected subject
        quiz_window = QuizWindow(selected_subject)
        quiz_window.mainloop()

    def go_back(self):
        from student_dashboard import StudentDashboard
        self.withdraw()
        student_dashboard = StudentDashboard()
        student_dashboard.mainloop()

class QuizWindow(ctk.CTk):
    def __init__(self, selected_subject):
        super().__init__()

        self.title("Quiz")
        self.selected_subject = selected_subject
        self.questions = DatabaseOperation().get_quiz_questions(selected_subject)

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

        back_button1 = ctk.CTkButton(self, text="\u2190", command=self.go_back, width=30, height=30)
        back_button1.pack(side="top", anchor="nw", padx=10, pady=10)

        # Center the window on the screen
        self.center_window()

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
            # Show the back button when all questions are answered
            self.back_button.pack(pady=10)

    def answer_question(self, selected_option):
        correct_option = self.questions[self.current_question_index][-1]

        if selected_option == correct_option:
            self.correct_answers += 1

        self.current_question_index += 1
        self.update_question()

    def show_result(self):
        self.question_label.configure(text=f"Quiz completed!\nYou scored {self.correct_answers}/{len(self.questions)}")

    def go_back(self):
        from student_dashboard import StudentDashboard 
        # Close the quiz window
        self.withdraw()

        # Open the student dashboard window
       # student_dashboard = StudentDashboard()
       # student_dashboard.mainloop()

    def center_window(self):
        # Get the screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the position of the window
        x_position = (screen_width - self.winfo_reqwidth()) // 2
        y_position = (screen_height - self.winfo_reqheight()) // 2

        # Set the window position
        self.geometry(f"+{x_position}+{y_position}")

if __name__ == "__main__":
    app = AttemptQuizSubject()
    app.mainloop()
'''

import customtkinter as ctk
from database_operation import DatabaseOperation 


def obtain_student_id():
    from student_login import StudentLogin
    # Create an instance of the StudentLogin class
    login_screen = StudentLogin()

    # Start the login screen's main loop
    login_screen.mainloop()

    # After the main loop finishes (e.g., after successful login), retrieve the student ID
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

        window_width = 600
        window_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        back_button = ctk.CTkButton(self, text="\u2190", command=self.go_back, width=30, height=30)
        back_button.pack(side="top", anchor="nw", padx=10, pady=10)

        select_subject_label = ctk.CTkLabel(self, text="Select Subject", font=("Helvetica", 20))
        select_subject_label.pack(pady=20)

        subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
        self.subject_var = ctk.StringVar(value=subjects[0])

        def subject_dropdown_callback(choice):
            self.subject_var.set(choice)

        subject_dropdown = ctk.CTkOptionMenu(self, values=subjects, command=subject_dropdown_callback, variable=self.subject_var)
        subject_dropdown.pack(pady=10)

        instructions_label = ctk.CTkLabel(self, text="Read the instructions below before starting the quiz:", font=("Helvetica", 15))
        instructions_label.pack(pady=10)

        instructions_text = """
        1. This quiz consists of multiple-choice questions.
        2. Select the correct answer for each question.
        3. You cannot go back to previous questions, so answer carefully.
        4. Click the 'Start Quiz' button when you are ready.
        """

        instructions_text_label = ctk.CTkLabel(self, text=instructions_text, font=("Helvetica", 15), justify=ctk.LEFT, wraplength=500)
        instructions_text_label.pack(pady=20)

        start_quiz_button = ctk.CTkButton(self, text="Start Quiz", command=self.start_quiz)
        start_quiz_button.pack(pady=20)

    def start_quiz(self):
        # Get the selected subject
        selected_subject = self.subject_var.get()

        # Debug print
        print(f"Student ID before starting quiz: {self.student_id}")
        
        # Close the subject selection window
        self.withdraw()
        
        # Open the quiz window for the selected subject and pass the student ID
        quiz_window = QuizWindow(self.student_id, selected_subject)
        quiz_window.mainloop()

    def go_back(self):
        from student_dashboard import StudentDashboard  # Import StudentDashboard class
        student_dashboard = StudentDashboard(self.student_id)  # Pass the student ID back to the StudentDashboard
        self.withdraw()
        student_dashboard.mainloop()

class QuizWindow(ctk.CTk):
    def __init__(self, student_id, selected_subject):
        super().__init__()

        self.title("Quiz")
        self.student_id = student_id
        self.selected_subject = selected_subject
        self.questions = DatabaseOperation().get_quiz_questions(selected_subject)

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
        
        # Display the score
        score_text = f"Quiz completed!\nYou scored {self.correct_answers}/{len(self.questions)}"
        score_label = ctk.CTkLabel(self, text=score_text, font=("Helvetica", 14))
        score_label.pack(pady=20)

        # Store the score in the database
        database = DatabaseOperation()
        database.add_score(self.student_id, self.selected_subject, self.correct_answers)

        # Show the back button
        back_button = ctk.CTkButton(self, text="\u2190", command=self.go_back, width=30, height=30)
        back_button.pack(side="top", anchor="nw", padx=10, pady=10)

    def go_back(self):
        from student_dashboard import StudentDashboard
        student_dashboard = StudentDashboard(self.student_id)
        self.withdraw()
        student_dashboard.mainloop()

if __name__ == "__main__":
    student_id = obtain_student_id()  # Replace this with the actual student ID
    app = AttemptQuizSubject(student_id)
    app.mainloop()

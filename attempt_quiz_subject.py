#test for selecting subject
import customtkinter as ctk

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
        # Implement the functionality to start the quiz for the selected subject
        selected_subject = self.subject_var.get()
        print(f"Starting quiz for {selected_subject}")

    def go_back(self):
        from student_dashboard import StudentDashboard
        self.destroy()
        student_dashboard = StudentDashboard()
        student_dashboard.mainloop()


if __name__ == "__main__":
    app = AttemptQuizSubject()
    app.mainloop()

import customtkinter as ctk

class StudyMaterial(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.title("Study Material")

        # Set the size of the window and center it
        window_width = 800
        window_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Define links for each subject
        subject_links = [
            ["Link 1 for Subject 1", "Link 2 for Subject 1", "Link 3 for Subject 1", "Link 4 for Subject 1", "Link 5 for Subject 1"],
            ["Link 1 for Subject 2", "Link 2 for Subject 2", "Link 3 for Subject 2", "Link 4 for Subject 2", "Link 5 for Subject 2"],
            ["Link 1 for Subject 3", "Link 2 for Subject 3", "Link 3 for Subject 3", "Link 4 for Subject 3", "Link 5 for Subject 3"],
            ["Link 1 for Subject 4", "Link 2 for Subject 4", "Link 3 for Subject 4", "Link 4 for Subject 4", "Link 5 for Subject 4"],
            ["Link 1 for Subject 5", "Link 2 for Subject 5", "Link 3 for Subject 5", "Link 4 for Subject 5", "Link 5 for Subject 5"],
        ]

        # Creating five sections
        for section_number, links in enumerate(subject_links, start=1):
            section_frame = ctk.CTkFrame(self)
            section_frame.pack(side="left", fill="both", expand=True)

            # Adding a label to each section
            section_label = ctk.CTkLabel(section_frame, text=f"Subject {section_number}", font=("Helvetica", 16))
            section_label.pack(pady=10)

            # Adding five website links to each section
            for link_number, link_text in enumerate(links, start=1):
                website_link = ctk.CTkLabel(section_frame, text=link_text, fg="blue", cursor="hand2")
                website_link.bind("<Button-1>", lambda event, link=link_text: self.open_link(link))
                website_link.pack()

    def open_link(self, link):
        # Implement the functionality to open the link in a browser
        # For demonstration purposes, it prints the selected link
        print(f"Opening link: {link}")

if __name__ == "__main__":
    app = StudyMaterial()
    app.mainloop()

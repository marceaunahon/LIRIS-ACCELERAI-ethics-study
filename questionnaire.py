import customtkinter as ctk
import numpy as np
from data_parser import read_questions
from question import Question
from typing import List

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

class Questionnaire(ctk.CTk):

    def __init__(self, questions : List[Question]):
        super().__init__()
        self.iconbitmap('Images/liris.ico')
        self.title("Questionnaire utilisateur")
        self.geometry("500x800")
        self.questions = questions
        self.title_label = ctk.CTkLabel(self, text="Quel utilisateur êtes vous ?", font=ctk.CTkFont(size=30, weight="bold"))
        self.title_label.place(relx=0.5, rely=0.04, anchor="center")
        self.main_frame = MainFrame(self, relx = 0.5, rely = 0.5, relwidth = 0.9, relheight=0.83)
        self.button = ctk.CTkButton(self, text="Confirmer", command=self.save)
        self.button.place(relx = 0.8, rely=0.95, anchor = "center")
        self.results = np.zeros(9, dtype="U200")

    def save(self):
        self.results[0] = self.main_frame.q1.get()
        self.results[1] = self.main_frame.q2.get()
        self.results[2] = self.main_frame.q3.get()
        self.results[3] = self.main_frame.q4.get()
        self.results[4] = self.main_frame.q5.get()
        self.results[5] = self.main_frame.q6.get()
        self.results[6] = self.main_frame.q7.get()
        self.results[7] = self.main_frame.q8.get()
        self.results[8] = self.main_frame.entry.get("0.0","end")
        self.destroy()

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent: Questionnaire, relx : float, rely : float, relwidth : float, relheight : float):
        super().__init__(master=parent, corner_radius=0)
        self.place(relx = relx, rely = rely, relwidth = relwidth, relheight=relheight, anchor="center")
        self.font = ctk.CTkFont(size=16, weight="bold")

        self.q1 = ctk.StringVar(value="")
        self.q1_label = ctk.CTkLabel(self, text=parent.questions[0].title, font=self.font)
        self.q1_label.place(relx=0.5, rely=0.05, anchor="center")
        self.q1_menu = ctk.CTkOptionMenu(self, values=parent.questions[0].answers_list, variable=self.q1)
        self.q1_menu.place(relx=0.5, rely=0.1, anchor="center")

        self.q2 = ctk.StringVar(value="")
        self.q2_label = ctk.CTkLabel(self, text=parent.questions[1].title, font=self.font)
        self.q2_label.place(relx=0.5, rely=0.15, anchor="center")
        self.q2_menu = ctk.CTkOptionMenu(self, values=parent.questions[1].answers_list, variable=self.q2)
        self.q2_menu.place(relx=0.5, rely=0.2, anchor="center")

        self.q3 = ctk.StringVar(value="")
        self.q3_label = ctk.CTkLabel(self, text=parent.questions[2].title, font=self.font)
        self.q3_label.place(relx=0.5, rely=0.25, anchor="center")
        self.q3_menu = ctk.CTkOptionMenu(self, values=parent.questions[2].answers_list, variable=self.q3)
        self.q3_menu.place(relx=0.5, rely=0.3, anchor="center")

        self.q4 = ctk.StringVar(value="")
        self.q4_label = ctk.CTkLabel(self, text=parent.questions[3].title, font=self.font)
        self.q4_label.place(relx=0.5, rely=0.35, anchor="center")
        self.q4_menu = ctk.CTkOptionMenu(self, values=parent.questions[3].answers_list, variable=self.q4)
        self.q4_menu.place(relx=0.5, rely=0.4, anchor="center")

        self.q5 = ctk.StringVar(value="")
        self.q5_label = ctk.CTkLabel(self, text=parent.questions[4].title, font=self.font)
        self.q5_label.place(relx=0.5, rely=0.45, anchor="center")
        self.q5_menu = ctk.CTkOptionMenu(self, values=parent.questions[4].answers_list, variable=self.q5)
        self.q5_menu.place(relx=0.5, rely=0.5, anchor="center")

        self.q6 = ctk.StringVar(value="")
        self.q6_label = ctk.CTkLabel(self, text=parent.questions[5].title, font=self.font)
        self.q6_label.place(relx=0.5, rely=0.55, anchor="center")
        self.q6_menu = ctk.CTkOptionMenu(self, values=parent.questions[5].answers_list, variable=self.q6)
        self.q6_menu.place(relx=0.5, rely=0.6, anchor="center")

        self.q7 = ctk.StringVar(value="")
        self.q7_label = ctk.CTkLabel(self, text=parent.questions[6].title, font=self.font)
        self.q7_label.place(relx=0.5, rely=0.65, anchor="center")
        self.q7_menu = ctk.CTkOptionMenu(self, values=parent.questions[6].answers_list, variable=self.q7)
        self.q7_menu.place(relx=0.5, rely=0.7, anchor="center")

        self.q8 = ctk.StringVar(value="")
        self.q8_label = ctk.CTkLabel(self, text=parent.questions[7].title, font=self.font)
        self.q8_label.place(relx=0.5, rely=0.75, anchor="center")
        self.q8_menu = ctk.CTkOptionMenu(self, values=parent.questions[7].answers_list, variable=self.q8)
        self.q8_menu.place(relx=0.5, rely=0.8, anchor="center")

        self.entry_label = ctk.CTkLabel(self, text="Avez-vous des besoins spécifiques (santé, télétravail) ?", font = self.font)
        self.entry = ctk.CTkTextbox(self)
        self.entry_label.place(relx=0.5, rely=0.85, anchor="center")
        self.entry.place(relx=0.5, rely=0.89, relwidth = 0.9, relheight = 0.07, anchor="n")

if __name__ == "__main__":
    questions = read_questions("data/questions.csv")
    app = Questionnaire(questions)
    app.mainloop()
    a = app.results
    print(a)

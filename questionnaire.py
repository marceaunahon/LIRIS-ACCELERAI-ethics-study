import customtkinter as ctk
import numpy as np

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

class Questionnaire(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.iconbitmap('Images/liris.ico')
        self.title("Questionnaire utilisateur")
        self.geometry("500x800")
        self.title_label = ctk.CTkLabel(self, text="Quel utilisateur êtes vous ?", font=ctk.CTkFont(size=30, weight="bold"))
        self.title_label.place(relx=0.5, rely=0.04, anchor="center")
        self.main_frame = MainFrame(self)
        self.button = ctk.CTkButton(self, text="Confirmer", command=self.save)
        self.button.place(relx = 0.8, rely=0.95, anchor = "center")
        self.results = np.zeros(9, dtype="U200")

    def save(self):
        self.results[0] = self.main_frame.age.get()
        self.results[1] = self.main_frame.job.get()
        self.results[2] = self.main_frame.number.get()
        self.results[3] = self.main_frame.week_day.get()
        self.results[4] = self.main_frame.week_night.get()
        self.results[5] = self.main_frame.weekend_day.get()
        self.results[6] = self.main_frame.weekend_night.get()
        self.results[7] = self.main_frame.residence.get()
        self.results[8] = self.main_frame.entry.get("0.0","end")
        self.destroy()

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent: Questionnaire):
        super().__init__(master=parent, corner_radius=0) #,fg_color="transparent")
        self.place(relx = 0.5, rely = 0.5, relwidth = 0.9, relheight=0.83, anchor="center")
        self.font = ctk.CTkFont(size=16, weight="bold")

        self.age = ctk.StringVar(value="Faire un choix")
        self.age_label = ctk.CTkLabel(self, text="Tranche d'âge", font=self.font)
        self.age_label.place(relx=0.5, rely=0.05, anchor="center")
        self.age_menu = ctk.CTkOptionMenu(self, values=["18 - 24 ans", "25 - 34 ans", "35 - 49 ans", "50 - 64 ans", "65 et plus"], variable=self.age)
        self.age_menu.place(relx=0.5, rely=0.1, anchor="center")

        self.job = ctk.StringVar(value="Faire un choix")
        self.job_label = ctk.CTkLabel(self, text="Catégorie socio-professionelle", font=self.font)
        self.job_label.place(relx=0.5, rely=0.15, anchor="center")
        self.job_menu = ctk.CTkOptionMenu(self, values=["Agriculteurs exploitants", "Artisans, commerçants et chefs d'entreprise",
                                                        "Cadres et professions intellectuelles supérieures", "Professions intermédiaires",
                                                        "Employés", "Ouvriers", "Retraités",
                                                        "Autres personnes sans activité professionelle"], variable=self.age)
        self.job_menu.place(relx=0.5, rely=0.2, anchor="center")

        self.number = ctk.StringVar(value="Faire un choix")
        self.number_label = ctk.CTkLabel(self, text="Avec combien de personnes vivez-vous ?", font=self.font)
        self.number_label.place(relx=0.5, rely=0.25, anchor="center")
        self.number_menu = ctk.CTkOptionMenu(self, values=["0", "1", "2", "3", "4", "5", "6 et plus"], variable=self.number)
        self.number_menu.place(relx=0.5, rely=0.3, anchor="center")

        self.week_day = ctk.StringVar(value="Faire un choix")
        self.week_day_label = ctk.CTkLabel(self, text="En semaine, êtes-vous présent(e) la journée ?", font=self.font)
        self.week_day_label.place(relx=0.5, rely=0.35, anchor="center")
        self.week_day_menu = ctk.CTkOptionMenu(self, values=["Oui", "Non", "Variable"], variable=self.week_day)
        self.week_day_menu.place(relx=0.5, rely=0.4, anchor="center")

        self.week_night = ctk.StringVar(value="Faire un choix")
        self.week_night_label = ctk.CTkLabel(self, text="En semaine, êtes-vous présent(e) la nuit ?", font=self.font)
        self.week_night_label.place(relx=0.5, rely=0.45, anchor="center")
        self.week_night_menu = ctk.CTkOptionMenu(self, values=["Oui", "Non", "Variable"], variable=self.week_night)
        self.week_night_menu.place(relx=0.5, rely=0.5, anchor="center")

        self.weekend_day = ctk.StringVar(value="Faire un choix")
        self.weekend_day_label = ctk.CTkLabel(self, text="En week-end, êtes-vous présent(e) la journée ?", font=self.font)
        self.weekend_day_label.place(relx=0.5, rely=0.55, anchor="center")
        self.weekend_day_menu = ctk.CTkOptionMenu(self, values=["Oui", "Non", "Variable"], variable=self.weekend_day)
        self.weekend_day_menu.place(relx=0.5, rely=0.6, anchor="center")

        self.weekend_night = ctk.StringVar(value="Faire un choix")
        self.weekend_night_label = ctk.CTkLabel(self, text="En week-end, êtes-vous présent(e) la nuit ?", font=self.font)
        self.weekend_night_label.place(relx=0.5, rely=0.65, anchor="center")
        self.weekend_night_menu = ctk.CTkOptionMenu(self, values=["Oui", "Non", "Variable"], variable=self.weekend_night)
        self.weekend_night_menu.place(relx=0.5, rely=0.7, anchor="center")

        self.residence = ctk.StringVar(value="Faire un choix")
        self.residence_label = ctk.CTkLabel(self, text="Il s'agit de votre résidence :", font=self.font)
        self.residence_label.place(relx=0.5, rely=0.75, anchor="center")
        self.residence_menu = ctk.CTkOptionMenu(self, values=["Principale", "Secondaire"], variable=self.residence)
        self.residence_menu.place(relx=0.5, rely=0.8, anchor="center")

        self.entry_label = ctk.CTkLabel(self, text="Avez-vous des besoins spécifiques (santé, télétravail) ?", font = self.font)
        self.entry = ctk.CTkTextbox(self)
        self.entry_label.place(relx=0.5, rely=0.85, anchor="center")
        self.entry.place(relx=0.5, rely=0.89, relwidth = 0.9, relheight = 0.07, anchor="n")

if __name__ == "__main__":
    app = Questionnaire()
    app.mainloop()
    a = app.results
    print(a)

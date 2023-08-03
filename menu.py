import customtkinter as ctk
from typing import List
from situation import Value, ChoiceSituation
from data import read_values_and_situations
import numpy as np
from CTkMessagebox import CTkMessagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

class Menu(ctk.CTk):

    def __init__(self, values_list: List[Value], 
                 values_list_name_only : List[str],
                 situation_list : List[ChoiceSituation],
                 title : str = "menu", 
                 size : List[int] = [500,700]):
        super().__init__()
        self.iconbitmap('Images/liris.ico')
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")

        self.values = values_list
        self.values_name_only = values_list_name_only
        self.situation_list = situation_list
        self.font20 = ctk.CTkFont(size=20, weight="bold")
        self.font18 = ctk.CTkFont(size=18, weight="bold")
        self.font16 = ctk.CTkFont(size=16, weight="bold")
        self.experiment_frame = ExperimentsFrame(self)
        self.values_frame = ValuesFrame(self)
        self.confirm = ctk.CTkButton(master=self, text="Confirmer", command=self.next)
        self.confirm.place(relx=0.5, rely=0.92, anchor="center")

        self.global_param = np.zeros(9)
        self.sliders_param = 2
        self.choice_param = np.zeros(4)
        self.selected_values = []
        self.selected_values_name_only = []
        self.selected_situations = []


    def save(self):
        #On remplit la liste des paramètres
        self.store_params()
        #On stocke toutes les valeurs sélectionnées
        self.store_values()
        #On selectionne les situations correspondant aux valeurs choisies et au nombre de situation par couple de valeur
        self.store_situations()
        #On stocke les choix de l'utilisateur
        self.store_menu_choices()

        
    def store_params(self):
        self.global_param[0] = self.experiment_frame.questionnaire.get()
        self.global_param[1] = self.experiment_frame.sliders.get()
        self.global_param[2] = self.experiment_frame.choice.get()
        self.global_param[3] = self.experiment_frame.acceptability.get()

        self.choice_param[0] = self.experiment_frame.use_diff.get()
        self.choice_param[1] = self.experiment_frame.use_rel.get()
        self.choice_param[2] = self.experiment_frame.disp_values.get()
        self.choice_param[3] = self.experiment_frame.number.get()

    def store_values(self):
        for i in range(len(self.values)):
             if self.values_frame.values_variables[i].get() == 1:
                  for j in range(len(self.values)):
                       if str(self.values_frame.values_variables[i]) == self.values_name_only[j]:
                            self.selected_values.append(self.values[j])
                            self.selected_values_name_only.append(self.values_name_only[j])

    def store_situations(self):
        temp_situations = []
        if self.experiment_frame.number.get() == 1:
            temp_situations = self.situation_list[0:15]
        if self.experiment_frame.number.get() == 2:
            temp_situations = self.situation_list[0:30]
        if self.experiment_frame.number.get() == 3:
            temp_situations = self.situation_list[0:45]
        if self.experiment_frame.number.get() == 3:
            temp_situations = self.situation_list[0:60]
        if self.experiment_frame.number.get() == 3:
            temp_situations = self.situation_list[0:75]
        for situation in temp_situations:
            if situation.value1 in self.selected_values and situation.value2 in self.selected_values:
                self.selected_situations.append(situation)

    def store_menu_choices(self):
        self.list = []
        self.selected_situations_str = np.zeros(len(self.selected_situations), dtype=ChoiceSituation)
        for i in range(len(self.selected_situations)):
            self.selected_situations_str[i] = str(self.selected_situations[i])
        self.selected_values_str = np.zeros(len(self.selected_values), dtype=Value)
        for i in range(len(self.selected_values)):
            self.selected_values_str[i] = str(self.selected_values[i])
        self.list.append(self.global_param)
        self.list.append(self.choice_param)
        self.list.append(self.selected_values_str)
        self.list.append(self.selected_situations_str)

        

    def next(self):
        self.save()
        if (len(self.selected_values) < 2) and not(self.global_param[2] == self.global_param[3] == 0):
            CTkMessagebox(title="Erreur",message="Veuillez choisir au moins deux valeurs", icon="cancel")
            self.selected_values = []
        else :
            self.destroy()

class ExperimentsFrame(ctk.CTkFrame):

    def __init__(self, parent : Menu):
        super().__init__(master = parent)
        self.place(relx=0.02, rely=0.05, relwidth = 0.47, relheight = 0.8)
        self.title = ctk.CTkLabel(master=self, text="Applications", font=parent.font20)
        self.title.place(relx=0.5, rely=0.1, anchor="center")

        #Choix des applications
        self.questionnaire = ctk.IntVar()
        self.sliders = ctk.IntVar()
        self.choice = ctk.IntVar()
        self.acceptability = ctk.IntVar()
        self.choose_questionnaire = ctk.CTkCheckBox(master=self, text="Questionnaire utilisateur", variable=self.questionnaire)
        self.choose_sliders = ctk.CTkCheckBox(master=self, text="Questionnaire valeur", variable=self.sliders,
                                              command=self.change_param_state)
        self.choose_choice = ctk.CTkCheckBox(master=self, text="Choix en situation ", variable=self.choice, 
                                             command=self.change_param_state)
        self.choose_acceptability = ctk.CTkCheckBox(master=self, text="Acceptabilité", variable=self.acceptability,
                                                    command=self.change_param_state)

        #Paramètres
        self.disp_values = ctk.IntVar()
        self.use_diff = ctk.IntVar()
        self.use_rel = ctk.IntVar()
        self.choose_disp_values = ctk.CTkCheckBox(master=self, text="Montrer les valeurs", variable=self.disp_values)
        self.choose_use_diff = ctk.CTkCheckBox(master=self, text="Demander la difficulté", variable=self.use_diff)
        self.choose_use_rel = ctk.CTkCheckBox(master=self, text="Demander la pertinence", variable=self.use_rel)
        self.number = ctk.IntVar(value=1) #le nombre de situations par couple de valeurs

        #Placement des widgets
        self.choose_questionnaire.place(relx=0.15, rely=0.22, anchor="w")
        self.choose_sliders.place(relx=0.15, rely=0.3, anchor="w")
        self.choose_choice.place(relx=0.15, rely=0.38, anchor="w")
        self.choose_disp_values.place(relx=0.2, rely=0.46, anchor="w")
        self.choose_use_diff.place(relx=0.2, rely=0.52, anchor="w")
        self.choose_use_rel.place(relx=0.2, rely=0.58, anchor="w")
        self.choose_acceptability.place(relx=0.15, rely=0.66, anchor="w")

        #Dernier bouton: nombre de dilemmes par couple de valeurs
        self.number_label = ctk.CTkLabel(self, text="Nombre de situations", font=parent.font16)
        self.number_label.place(relx=0.5, rely=0.78, anchor="center")
        self.number_menu = ctk.CTkOptionMenu(self, values=["1", "2", "3", "4", "5"], variable=self.number)
        self.number_menu.place(relx=0.5, rely=0.84, anchor="center")

        #Configuration des widgets initialement grisés
        self.choose_disp_values.configure(state="disabled")
        self.choose_use_diff.configure(state="disabled")
        self.choose_use_rel.configure(state="disabled")
        self.number_menu.configure(state="disabled")
        self.number.set(0)

    def change_param_state(self):
        if self.choice.get() == 1 or self.acceptability.get() == 1:
            self.number_menu.configure(state="normal")
            self.number.set(1)
        if self.choice.get() == 0 and self.acceptability.get() == 0:
            self.number_menu.configure(state="disabled")
            self.number.set(0)
        if self.choice.get() == 0:
            self.choose_disp_values.configure(state="disabled")
            self.choose_use_diff.configure(state="disabled")
            self.choose_use_rel.configure(state="disabled")
            self.disp_values.set(0)
            self.use_diff.set(0)
            self.use_rel.set(0)
        if self.choice.get() == 1:
            self.choose_disp_values.configure(state="normal")
            self.choose_use_diff.configure(state="normal")
            self.choose_use_rel.configure(state="normal")
            self.use_diff.set(1)
            self.use_rel.set(1)

class ValuesFrame(ctk.CTkFrame):

    def __init__(self, parent : Menu):
        super().__init__(master = parent)
        self.a = []
        self.place(relx=0.51, rely=0.05, relwidth = 0.47, relheight = 0.8)
        self.title = ctk.CTkLabel(master=self, text="Valeurs", font=parent.font20)
        self.title.place(relx=0.5, rely=0.1, anchor="center")

        #initialisation des variables
        self.all = ctk.IntVar() #toutes les valeurs sont choisies
        self.inclusiveness = ctk.IntVar(name="Inclusiveness")
        self.well_being = ctk.IntVar(name="Well-being")
        self.environmetal_sustainability = ctk.IntVar(name="Environmental sustainability")
        self.privacy = ctk.IntVar(name="Privacy")
        self.security_of_supply = ctk.IntVar(name="Security of supply")
        self.affordability = ctk.IntVar(name="Affordability")
        self.values_variables = [self.inclusiveness, self.well_being, self.environmetal_sustainability,
                             self.privacy, self.security_of_supply, self.affordability]
        

        #Création des boutons correspondant à chaque valeur
        self.all_button = ctk.CTkCheckBox(master=self, text="Toutes", variable=self.all, command=self.check_all, font=parent.font18)
        self.inclusiveness_button = ctk.CTkCheckBox(master=self, text="Inclusiveness", 
                                                    variable=self.inclusiveness, command=self.uncheck_all)
        self.well_being_button = ctk.CTkCheckBox(master=self, text="Well-being", 
                                                 variable=self.well_being, command=self.uncheck_all)
        self.environmetal_sustainability_button = ctk.CTkCheckBox(master=self, text="Environmental sustainability", 
                                                                  variable=self.environmetal_sustainability, command=self.uncheck_all)
        self.privacy_button = ctk.CTkCheckBox(master=self, text="Privacy", 
                                              variable=self.privacy, command=self.uncheck_all)
        self.security_of_supply_button = ctk.CTkCheckBox(master=self, text="Security of supply", 
                                                         variable=self.security_of_supply, command=self.uncheck_all)
        self.affordability_button = ctk.CTkCheckBox(master=self, text="Affordability", variable=self.affordability, 
                                                    command=self.uncheck_all)


        #Placement des boutons
        self.all_button.place(relx = 0.15, rely = 0.22, anchor="w")
        self.inclusiveness_button.place(relx = 0.15, rely = 0.34, anchor="w")
        self.well_being_button.place(relx = 0.15, rely = 0.42, anchor="w")
        self.environmetal_sustainability_button.place(relx = 0.15, rely = 0.5, anchor="w")
        self.privacy_button.place(relx = 0.15, rely = 0.58, anchor="w")
        self.security_of_supply_button.place(relx = 0.15, rely = 0.66, anchor="w")
        self.affordability_button.place(relx = 0.15, rely = 0.74, anchor="w")

    def check_all(self):
        if self.all.get() == 1 :
            for vv in self.values_variables:
                    vv.set(1)
        if self.all.get() == 0 :
            for vv in self.values_variables:
                    vv.set(0)

    def uncheck_all(self):
        for vv in self.values_variables:
            if vv.get() == 0:
                self.all.set(0)

if __name__ == "__main__":
    values, values_name_only, situation_list = read_values_and_situations("data/values.csv", "data/situations.csv")
    app = Menu(values, values_name_only, situation_list)
    app.mainloop()

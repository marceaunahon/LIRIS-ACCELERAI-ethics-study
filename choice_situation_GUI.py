import numpy as np
import customtkinter as ctk
from data import read_values_and_situations, store
from situation import ChoiceSituation
from PIL import Image
from typing import List
from CTkMessagebox import CTkMessagebox
from general_GUI import GeneralGUI


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

class ChoiceSituationGUI(GeneralGUI):

    def __init__(self, situation_list: List[ChoiceSituation], title : str = "GUI", 
                 size : List[int] = [1200,700], use_difficulty = True, use_relevance = True,
                 disp_values = False):
        #disp_values = False : les valeurs sont cachées (état par défaut)
        #disp_values = True : les valeurs sont affichées
        #threshold = True : mode seuil d'acceptabilité
        super().__init__(situation_list, title, size)
        self.iconbitmap('Images/liris.ico')
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")

        #Options
        self.disp_values = disp_values
        self.use_difficulty = use_difficulty
        self.use_relevance = use_relevance

        #Creation des listes
        self.choices = np.zeros(len(situation_list)) #liste des choix effectués pour chaque situation (0 : solution A, 1 : solution B)
        self.difficulties = np.zeros(len(situation_list)) #liste des difficultés pour chaque prise de décision (de 0 à 1)
        self.relevances = np.zeros(len(situation_list)) #liste des pertinences de chaque situation
        self.weights = np.zeros(len(situation_list)) #liste des poids accordés à la valeur ayant remporté la confrontation

        if self.use_difficulty and self.use_relevance :
            self.results = np.zeros((len(situation_list),4))
        elif self.use_difficulty or self.use_relevance :
            self.results = np.zeros((len(situation_list),3))
        else :
            self.results = np.zeros((len(situation_list),2))

        #Création des variables
        self.choice = ctk.IntVar() #choix fait par l'utilisateur
        self.difficulty = ctk.DoubleVar() #difficulté de prise de décision
        self.difficulty_str = ctk.StringVar() #difficulté affichée en texte pour une meilleure compréhension de l'utilisateur
        self.relevance = ctk.DoubleVar() #pertinence de la situation
        self.relevance_str = ctk.StringVar() #pertinence affichée en texte pour une meilleure compréhension de l'utilisateur

        #Création de l'interface
        self.upper_frame = UpperFrame(self)
        self.lower_frame = LowerFrame(self)
        self.var_int_to_string() #affiche les variables des sliders en texte pour une meilleure compréhension de l'utilisateur

    def save(self):
        #Une fois que l'utilisateur a fait son choix, il faut sauvegarder les données, on stocke donc :
        #Le choix de l'utilisateur (0 ou 1)
        #La difficulté du choix (de 0 à 1)
        #La pertinence de la situation (de 0 à 1)
        #L'identifiant de la situation (de 1 à len(situation_list))
        self.choices[self.situation_count]=self.choice.get()
        #if self.use_difficulty:
        self.difficulties[self.situation_count]=self.difficulty.get()
        #if self.use_relevance:
        self.relevances[self.situation_count]=self.relevance.get()
        self.id[self.situation_count]=self.situation.id
        #Pour le poids, il faut le changer en fonction du nombre de niveaux de difficulté et des valeurs de difficulté maximale et minimale

        #On stocke tous les résultats dans un liste
        # if self.use_difficulty and self.use_relevance :
        self.results[self.situation_count][0] = self.id[self.situation_count]
        self.results[self.situation_count][1] = self.choices[self.situation_count]
        self.results[self.situation_count][2] = self.difficulties[self.situation_count]
        self.results[self.situation_count][3] = self.relevances[self.situation_count]
        # elif self.use_difficulty:
        #     self.results[self.situation_count][0] = self.id[self.situation_count]
        #     self.results[self.situation_count][1] = self.choices[self.situation_count]
        #     self.results[self.situation_count][2] = self.difficulties[self.situation_count]
        # elif self.use_relevance:
        #     self.results[self.situation_count][0] = self.id[self.situation_count]
        #     self.results[self.situation_count][1] = self.choices[self.situation_count]
        #     self.results[self.situation_count][2] = self.relevances[self.situation_count]
        # else :
        #     self.results[self.situation_count][0] = self.id[self.situation_count]
        #     self.results[self.situation_count][1] = self.choices[self.situation_count]



    def set_weights(self, list):
        #Le poids accordé à la valeur gagnante dépend du nombre de niveaux de difficulté et de la technique de comparaison
        #Pour cette raison, on implémente un setter et on définit les poids hors de la classe
        self.weights = list
        return self.weights

    def var_int_to_string(self):
        #Pour l'affichage du slider, il semble plus comprehensible d'utiliser des indicateurs textuels,
        #plutot que les valeurs initiales comprises entre 0 et 1

        if self.difficulty.get() == 0.:
            self.difficulty_str.set("Très facile de choisir")
        if self.difficulty.get() == 1.:
            self.difficulty_str.set("Facile de choisir")
        if self.difficulty.get() == 2.:
            self.difficulty_str.set("Difficulté modérée")
        if self.difficulty.get() == 3.:
            self.difficulty_str.set("Difficile de choisir")
        if self.difficulty.get() == 4.:
            self.difficulty_str.set("Très difficile de choisir")

        if self.relevance.get() == 0.:
            self.relevance_str.set("Très peu pertinent")
        if self.relevance.get() == 1.:
            self.relevance_str.set("Peu pertinent")
        if self.relevance.get() == 2.:
            self.relevance_str.set("Pertinence modérée")
        if self.relevance.get() == 3.:
            self.relevance_str.set("Pertinent")
        if self.relevance.get() == 4.:
            self.relevance_str.set("Très pertinent pertinent")
        #On appelle la fonction tous les 200ms
        self.after(200, self.var_int_to_string)

    def reset(self):
        self.upper_frame.reset_upper_frame(self) #on réinitialise le cadre supérieur (présentation de la situation)
        self.lower_frame.reset_sliders(self) #on réinitialise le cadre inférieur (évaluation de la situation)

class UpperFrame(ctk.CTkFrame):

    def __init__(self, parent : ChoiceSituationGUI):
        #On construit le cadre supérieur (présentation de la situation)
        super().__init__(master = parent, corner_radius=0)
        self.place(x=0, y=0, relwidth = 1, relheight = 0.6)
        self.im1 = ImageCanvasLeft(self, GUI=parent) #on place l'image
        self.im2 = ImageCanvasRight(self, GUI=parent) #on place l'image
        self.textbox = TextBox(self, GUI=parent) #on place le texte

    def reset_upper_frame(self, GUI : ChoiceSituationGUI):
        self.textbox.reset_text(GUI) #on insère le nouveau texte
        self.im1.reset_image(GUI) #on insère la nouvelle image
        self.im2.reset_image(GUI)

class ImageCanvasLeft(ctk.CTkCanvas):

    def __init__(self, parent : UpperFrame, GUI : ChoiceSituationGUI):
        super().__init__(master=parent)
        #On construit le canvas
        self.place(relx = 0.01, rely=0.1, relwidth = 0.28, relheight=0.8)

        self.im = ctk.CTkImage(Image.open(GUI.situation.im1_path), size = (470,470))
        self.im_label = ctk.CTkLabel(master=self,image=self.im,text="") #on créé un label contenant l'image avec pour master le canvas
        self.im_label.place(relx=0.5,rely=0.5,anchor="center")

    def reset_image(self, GUI : ChoiceSituationGUI):
        self.im = ctk.CTkImage(Image.open(GUI.situation.im1_path), size = (470,470))
        self.im_label.configure(image=self.im)

class ImageCanvasRight(ctk.CTkCanvas):

    def __init__(self, parent : UpperFrame, GUI : ChoiceSituationGUI):
        super().__init__(master=parent)
        #On construit le canvas
        self.place(relx = 0.71, rely = 0.1, relwidth = 0.28, relheight = 0.8)
        self.im = ctk.CTkImage(Image.open(GUI.situation.im2_path), size = (470,470))
        self.im_label = ctk.CTkLabel(master=self,image=self.im,text="") #on créé un label contenant l'image avec pour master le canvas
        self.im_label.place(relx=0.5,rely=0.5,anchor="center")

    def reset_image(self, GUI : ChoiceSituationGUI):
        self.im = ctk.CTkImage(Image.open(GUI.situation.im2_path), size = (470,470))
        self.im_label.configure(image=self.im)

class TextBox(ctk.CTkTextbox):

    def __init__(self, parent : UpperFrame, GUI : ChoiceSituationGUI):
        #On construit la textbox
        font = ctk.CTkFont(family='Calibri', size = 20)
        super().__init__(master=parent, wrap="word", font=font, 
                         fg_color ="transparent", border_color="#33AE81", border_width =5)
        self.place(relx=0.31, rely=0.1, relwidth = 0.38, relheight = 0.8)
        self.adapt_text(GUI) ##on affiche les valeurs si disp_values = True
        self.insert("0.0", self.text) #on y insère l'énoncé de la situation
        self.configure(state='disabled') #on rend le texte accessible seulement en lecture

    def reset_text(self, GUI : ChoiceSituationGUI):
        self.adapt_text(GUI) #on affiche les valeurs si disp_values = True
        self.configure(state="normal") #on rend la textbox modifiable
        self.delete("0.0", "end") #on efface l'énoncé précédent
        self.insert("0.0",self.text) #on insère le nouvel énoncé
        self.configure(state="disabled") #on repasse la textbox en état non modifiable
        
    def adapt_text(self, GUI : ChoiceSituationGUI):
        self.text = GUI.situation.choice_statement
        if GUI.disp_values :
            # Si on a choisit d'afficher les valeurs on remplace Solution A et Solution B par les valeurs qu'elles représentent
            self.text = self.text.replace("(A)", f"({GUI.situation.value1.name_fr})")
            self.text = self.text.replace("(B)", f"({GUI.situation.value2.name_fr})")

class LowerFrame(ctk.CTkFrame):

    def __init__(self, parent : ChoiceSituationGUI):
        #On construit le cadre inférieur (évaluation de la situation)
        super().__init__(master = parent, corner_radius=0)
        self.place(relx=0, rely=0.6, relwidth = 1, relheight = 0.4)
        self.button_frame = EvalFrame(self, parent) 
        self.save_frame = SaveFrame(self, parent)
    
    def reset_sliders(self, GUI : ChoiceSituationGUI):
        self.button_frame.reset(GUI)

class EvalFrame(ctk.CTkFrame):

    def __init__(self, parent : ctk.CTkFrame, GUI : ChoiceSituationGUI):
        #On construit le cadre contenant les boutons et sliders de l'évaluation
        super().__init__(master = parent)
        self.font = ctk.CTkFont(size=20, weight="bold")
        self.font2 = ctk.CTkFont(size=16, weight="bold")
        self.place(relx=0.5, rely=0.31, relwidth = 0.6, relheight = 0.8, anchor="center")

        #Boutons et sliders utilisés en configuration de base
        self.solutionA = "Choix A"
        self.solutionB = "Choix B"
        self.b1 = ctk.CTkRadioButton(master=self, text = self.solutionA, font=self.font2, variable=GUI.choice, value=0)
        self.b2 = ctk.CTkRadioButton(master=self, text = self.solutionB, font=self.font2, variable=GUI.choice, value=1)
        self.label_difficulty = ctk.CTkLabel(master=self, text="Difficulté de décision", font=self.font)
        self.diff_slider = ctk.CTkSlider(self, from_=0, to=4, number_of_steps=4, variable = GUI.difficulty)
        self.diff_label = ctk.CTkLabel(self, textvariable=GUI.difficulty_str)
        self.label_relevance = ctk.CTkLabel(master=self, text="Pertinence de la situation", font=self.font)
        self.rel_slider = ctk.CTkSlider(self, from_=0, to=4, number_of_steps=4, variable = GUI.relevance)
        self.rel_label = ctk.CTkLabel(master=self, textvariable=GUI.relevance_str)

        #Configuration des boutons et sliders
        self.reset_values(GUI)
        if GUI.use_difficulty and GUI.use_relevance:
            self.b1.place(relx = 0.28, rely = 0.2, anchor="w")
            self.b2.place(relx = 0.64, rely = 0.2, anchor="w")
            self.label_difficulty.place(relx=0.5, rely = 0.4, anchor="center")
            self.diff_slider.place(relx=0.5, rely=0.5, anchor="center")
            self.diff_label.place(relx=0.5, rely=0.6, anchor="center")
            self.label_relevance.place(relx=0.5, rely = 0.7, anchor="center")
            self.rel_slider.place(relx=0.5, rely=0.8, anchor="center")
            self.rel_label.place(relx=0.5, rely=0.9, anchor="center")
        elif GUI.use_difficulty:
            self.b1.place(relx = 0.28, rely = 0.4, anchor="w")
            self.b2.place(relx = 0.64, rely = 0.4, anchor="w")
            self.label_difficulty.place(relx=0.5, rely = 0.6, anchor="center")
            self.diff_slider.place(relx=0.5, rely=0.7, anchor="center")
            self.diff_label.place(relx=0.5, rely=0.8, anchor="center")
        elif GUI.use_relevance:
            self.b1.place(relx = 0.28, rely = 0.4, anchor="w")
            self.b2.place(relx = 0.64, rely = 0.4, anchor="w")  
            self.label_relevance.place(relx=0.5, rely = 0.6, anchor="center")
            self.rel_slider.place(relx=0.5, rely=0.7, anchor="center")
            self.rel_label.place(relx=0.5, rely=0.8, anchor="center")
        else :
            self.b1.place(relx = 0.28, rely = 0.5, anchor="w")
            self.b2.place(relx = 0.64, rely = 0.5, anchor="w")

    def reset(self, GUI : ChoiceSituationGUI):
        self.reset_sliders(GUI)
        self.reset_values(GUI)

    def reset_sliders(self, GUI : ChoiceSituationGUI):
        self.diff_slider.set(0)
        self.rel_slider.set(0)
        GUI.choice.set(0)

    def reset_values(self, GUI : ChoiceSituationGUI):
        if GUI.disp_values:
            # Si on a choisit d'afficher les valeurs on remplace Solution A et Solution B par les valeurs qu'elles représentent
            self.b1.configure(text = f"{GUI.situation.value1.name_fr}")
            self.b2.configure(text = f"{GUI.situation.value2.name_fr}")

class SaveFrame(ctk.CTkFrame):
    def __init__(self, parent : ctk.CTkFrame, GUI : ChoiceSituationGUI):
        # On construit le cadre contenant les boutons "Suivant" et "Précédent"
        super().__init__(master=parent, fg_color="transparent")
        self.place(relx= 0.75, rely=0.75, relwidth=0.3, relheight=0.2)
        self.end = ctk.CTkButton(self, text="Suivant", text_color=("black", "white"), command=GUI.next)
        self.end.place(relx = 0.42, rely=0.5)
        self.back = ctk.CTkButton(self, text="Précédent", text_color=("black", "white"), command=GUI.previous)
        self.back.place(relx = 0, rely=0.5)

if __name__ == "__main__" : 
    values, values_name_only, situation_list = read_values_and_situations("data/values.csv", "data/situations.csv")
    interface = ChoiceSituationGUI(situation_list, use_difficulty=True, use_relevance=True, disp_values=False)
    interface.mainloop()
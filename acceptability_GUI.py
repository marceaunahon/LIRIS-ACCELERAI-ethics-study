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

class AcceptabilityGUI(GeneralGUI):

    def __init__(self, situation_list: List[ChoiceSituation], title : str = "GUI", 
                 size : List[int] = [1200,700], disp_values = False):
        #disp_values = False : les valeurs sont cachées (état par défaut)
        #disp_values = True : les valeurs sont affichées
        #threshold = True : mode seuil d'acceptabilité
        super().__init__(situation_list, title, size)
        self.iconbitmap('Images/liris.ico')
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")

        #Creation des listes
        self.acceptabilities = np.zeros(len(situation_list))
        self.value_changes = np.zeros(len(situation_list))
        self.results = np.zeros((len(situation_list), 2))

        #Création des variables
        self.acceptability = ctk.IntVar(value=1)
        self.value_change = ctk.IntVar(value=2)
        self.value_change_str = ctk.StringVar()

        #Options
        self.disp_values = disp_values

        #Création de l'interface
        self.upper_frame = UpperFrame(self)
        self.lower_frame = LowerFrame(self)
        self.var_int_to_string() #affiche les variables des sliders en texte pour une meilleure compréhension de l'utilisateur

    def save(self):
        #self.acceptabilities[self.situation_count] = self.acceptability.get()
        self.value_changes[self.situation_count] = self.value_change.get()

        #self.results[self.situation_count][0] = self.acceptabilities[self.situation_count]
        self.results[self.situation_count] = self.value_changes[self.situation_count]


    def var_int_to_string(self):
        #Pour l'affichage du slider, il semble plus comprehensible d'utiliser des indicateurs textuels,
        #plutot que les valeurs initiales comprises entre 0 et 1
        if self.value_change.get() == 0:
            self.value_change_str.set("Très satisfaisante, il ne faut pas intervenir")
        if self.value_change.get() == 1:
            self.value_change_str.set("Acceptable, pas besoin d'intervenir")
        if self.value_change.get() == 2:
            self.value_change_str.set("Difficile à juger, une intervention pourrait se justifer")
        if self.value_change.get() == 3:
            self.value_change_str.set("Pas satisfaisante, ce serait mieux d'intervenir")
        if self.value_change.get() == 4:
            self.value_change_str.set("Pas acceptable, il faut intervenir")

        self.after(200, self.var_int_to_string)

    def reset(self):
        self.upper_frame.reset_upper_frame(self) #on réinitialise le cadre supérieur (présentation de la situation)
        self.lower_frame.reset_sliders(self) #on réinitialise le cadre inférieur (évaluation de la situation)

class UpperFrame(ctk.CTkFrame):

    def __init__(self, parent : AcceptabilityGUI):
        #On construit le cadre supérieur (présentation de la situation)
        super().__init__(master = parent, corner_radius=0)
        self.place(x=0, y=0, relwidth = 1, relheight = 0.6)
        self.im1 = ImageCanvasLeft(self, GUI=parent) #on place l'image
        self.im2 = ImageCanvasRight(self, GUI=parent) #on place l'image
        self.textbox = TextBox(self, GUI=parent) #on place le texte

    def reset_upper_frame(self, GUI : AcceptabilityGUI):
        self.textbox.reset_text(GUI) #on insère le nouveau texte
        self.im1.reset_image(GUI) #on insère la nouvelle image
        self.im2.reset_image(GUI)

class ImageCanvasLeft(ctk.CTkCanvas):

    def __init__(self, parent : UpperFrame, GUI : AcceptabilityGUI):
        super().__init__(master=parent)
        #On construit le canvas
        self.place(relx = 0.01, rely=0.1, relwidth = 0.28, relheight=0.8)
        self.im = ctk.CTkImage(Image.open(GUI.situation.im1_path), size = (470,470))
        self.im_label = ctk.CTkLabel(master=self,image=self.im,text="") #on créé un label contenant l'image avec pour master le canvas
        self.im_label.place(relx=0.5,rely=0.5,anchor="center")

    def reset_image(self, GUI : AcceptabilityGUI):
        self.im = ctk.CTkImage(Image.open(GUI.situation.im1_path), size = (470,470))
        self.im_label.configure(image=self.im)

class ImageCanvasRight(ctk.CTkCanvas):

    def __init__(self, parent : UpperFrame, GUI : AcceptabilityGUI):
        super().__init__(master=parent)
        #On construit le canvas
        self.place(relx = 0.71, rely = 0.1, relwidth = 0.28, relheight = 0.8)
        self.im = ctk.CTkImage(Image.open(GUI.situation.im2_path), size = (470,470))
        self.im_label = ctk.CTkLabel(master=self,image=self.im,text="") #on créé un label contenant l'image avec pour master le canvas
        self.im_label.place(relx=0.5,rely=0.5,anchor="center")

    def reset_image(self, GUI : AcceptabilityGUI):
        self.im = ctk.CTkImage(Image.open(GUI.situation.im2_path), size = (470,470))
        self.im_label.configure(image=self.im)

class TextBox(ctk.CTkTextbox):

    def __init__(self, parent : UpperFrame, GUI : AcceptabilityGUI):
        #On construit la textbox
        font = ctk.CTkFont(family='Calibri', size = 20)
        super().__init__(master=parent, wrap="word", font=font, 
                         fg_color ="transparent", border_color="#33AE81", border_width =5)
        self.place(relx=0.31, rely=0.1, relwidth = 0.38, relheight = 0.8)
        self.adapt_text(GUI) #on affiche les valeurs si disp_values = True
        self.insert("0.0", self.text) #on y insère l'énoncé de la situation
        self.configure(state='disabled') #on rend le texte accessible seulement en lecture

    def reset_text(self, GUI : AcceptabilityGUI):
        self.adapt_text(GUI) #on affiche les valeurs si disp_values = True
        self.configure(state="normal") #on rend la textbox modifiable
        self.delete("0.0", "end") #on efface l'énoncé précédent
        self.insert("0.0",self.text) #on insère le nouvel énoncé
        self.configure(state="disabled") #on repasse la textbox en état non modifiable
        
    def adapt_text(self, GUI : AcceptabilityGUI):
        self.text = GUI.situation.threshold_statement

class LowerFrame(ctk.CTkFrame):

    def __init__(self, parent : AcceptabilityGUI):
        #On construit le cadre inférieur (évaluation de la situation)
        super().__init__(master = parent, corner_radius=0)
        self.place(relx=0, rely=0.6, relwidth = 1, relheight = 0.4)
        self.button_frame = EvalFrame(self, parent) 
        self.save_frame = SaveFrame(self, parent)
    
    def reset_sliders(self, GUI : AcceptabilityGUI):
        self.button_frame.reset(GUI)

class EvalFrame(ctk.CTkFrame):

    def __init__(self, parent : ctk.CTkFrame, GUI : AcceptabilityGUI):
        #On construit le cadre contenant les boutons et sliders de l'évaluation
        super().__init__(master = parent)
        self.font = ctk.CTkFont(size=20, weight="bold")
        self.font2 = ctk.CTkFont(size=16, weight="bold")
        self.place(relx=0.5, rely=0.31, relwidth = 0.6, relheight = 0.8, anchor="center")

        #Boutons et sliders utilisés en configuration "threshold"
        self.ok_or_not_ok = ctk.CTkLabel(master=self, text="Sans intervention de votre part, le sytème va agir", font=self.font)
        self.ok_or_not_ok.place(relx=0.5, rely=0.25, anchor="center")

        self.slider_label = ctk.CTkLabel(master=self, text="La décision du système est :", font=self.font2)
        self.slider_label.place(relx=0.5, rely = 0.5, anchor="center")
        self.slider = ctk.CTkSlider(self, from_=0, to=4, number_of_steps=4, variable=GUI.value_change)
        self.slider.place(relx=0.5, rely=0.65, anchor="center")
        self.variable_label = ctk.CTkLabel(master=self, textvariable=GUI.value_change_str, font=self.font2)
        self.variable_label.place(relx=0.5, rely = 0.8, anchor="center")

    def change_slider_state(self, GUI : AcceptabilityGUI):
        if GUI.acceptability.get() == 0:
            self.slider.configure(button_color="#33AE81", state="normal")
        if GUI.acceptability.get() == 1:
            self.slider.configure(button_color="#C0C0C0", state="disabled")
            self.slider.set(0)

    def reset(self, GUI : AcceptabilityGUI):
        #self.slider.configure(button_color="#C0C0C0", state="disabled")
        self.slider.set(0)
        GUI.acceptability.set(1)

class SaveFrame(ctk.CTkFrame):
    def __init__(self, parent : ctk.CTkFrame, GUI : AcceptabilityGUI):
        # On construit le cadre contenant les boutons "Suivant" et "Précédent"
        super().__init__(master=parent, fg_color="transparent")
        self.place(relx= 0.75, rely=0.75, relwidth=0.3, relheight=0.2)
        self.end = ctk.CTkButton(self, text="Suivant", text_color=("black", "white"), command=GUI.next)
        self.end.place(relx = 0.42, rely=0.5)
        self.back = ctk.CTkButton(self, text="Précédent", text_color=("black", "white"), command=GUI.previous)
        self.back.place(relx = 0, rely=0.5)

if __name__ == "__main__" : 
    values, values_name_only, situation_list = read_values_and_situations("data/values.csv", "data/situations2.csv")
    interface = AcceptabilityGUI(situation_list)
    interface.mainloop()

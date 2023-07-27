import customtkinter as ctk
import numpy as np
from PIL import Image
from CTkMessagebox import CTkMessagebox
from data import read_values_and_situations, Value
from typing import List
from definition_window import DefinitionWindow


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

class SlidersGUI(ctk.CTk):

    def __init__(self, all_values : List[Value], selected_values : List[Value]):
        super().__init__()
        self.iconbitmap('Images/liris.ico')
        self.title("Questionnaire valeurs")
        self.geometry("900x500")

        self.values = all_values
        self.selected_values = selected_values
        if self.values == selected_values: self.all = True
        else : self.all = False

        self.title_label = ctk.CTkLabel(self, text="Quelles valeurs sont importantes pour vous ?", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.place(relx=0.5, rely=0.05, anchor="center")
        self.first_frame = ValuesFrame(self, 0.25, 0.5, self.values[0], self.values[1], self.values[2])
        self.second_frame = ValuesFrame(self, 0.75, 0.5, self.values[3], self.values[4], self.values[5])
        self.button = ctk.CTkButton(self, text="Confirmer", command=self.save)
        self.button.place(relx = 0.5, rely=0.95, anchor = "center")

        self.results = np.zeros(len(self.values)) #a modifier par selected_values ? -> append ?

    def save(self):
        self.results[0] = self.first_frame.value1.get()
        self.results[1] = self.first_frame.value2.get()
        self.results[2] = self.first_frame.value3.get()
        self.results[3] = self.second_frame.value1.get()
        self.results[4] = self.second_frame.value2.get()
        self.results[5] = self.second_frame.value3.get()
        self.destroy()    

class ValuesFrame(ctk.CTkFrame):
    def __init__(self, parent: SlidersGUI,_relx, _rely, value1, value2, value3):
        super().__init__(master=parent)
        self.info_img = ctk.CTkImage(Image.open("Images/q.png"), size=(30,30))
        self.place(relx = _relx, rely= _rely, relwidth = 0.4, relheight = 0.75, anchor="center")
        self.font = ctk.CTkFont(size=16, weight="bold")

        self.value1_title = ctk.CTkLabel(master=self, text=value1.name_fr, font=self.font)
        self.value1_title.place(relx= 0.5, rely=0.14, anchor="center")
        self.value1_def_button = ctk.CTkButton(master=self, width=30, text="", fg_color = "transparent", 
                                               image=self.info_img, command = lambda: self.definition(value1))
        self.value1_def_button.place(relx = 0.9, rely=0.14, anchor="center")
        self.value1 = ctk.DoubleVar(value=0.5)
        self.value1_str = ctk.StringVar()
        self.slider1 = ctk.CTkSlider(self, from_=0, to=1, number_of_steps=6, variable=self.value1)
        self.slider1_label = ctk.CTkLabel(self, textvariable=self.value1_str)
        self.slider1.place(relx=0.5, rely=0.21, anchor="center")
        self.slider1_label.place(relx=0.5, rely=0.275, anchor="center")

        self.value2_title = ctk.CTkLabel(master=self, text=value2.name_fr, font=self.font)
        self.value2_title.place(relx= 0.5, rely=0.44, anchor="center")
        self.value2_def_button = ctk.CTkButton(master=self, width=30, text="", fg_color = "transparent", 
                                               image=self.info_img, command = lambda: self.definition(value2))
        self.value2_def_button.place(relx = 0.9, rely=0.44, anchor="center")
        self.value2 = ctk.DoubleVar(value=0.5)
        self.value2_str = ctk.StringVar()
        self.slider2 = ctk.CTkSlider(self, from_=0, to=1, number_of_steps=6, variable=self.value2)
        self.slider2_label = ctk.CTkLabel(self, textvariable=self.value2_str)
        self.slider2.place(relx=0.5, rely=0.51, anchor="center")
        self.slider2_label.place(relx=0.5, rely=0.575, anchor="center")

        self.value3_title = ctk.CTkLabel(master=self, text=value3.name_fr, font=self.font)
        self.value3_title.place(relx= 0.5, rely=0.74, anchor="center")
        self.value3_def_button = ctk.CTkButton(master=self, width=30, text="", fg_color = "transparent", 
                                               image=self.info_img, command = lambda: self.definition(value3))
        self.value3_def_button.place(relx = 0.9, rely=0.74, anchor="center")
        self.value3 = ctk.DoubleVar(value=0.5)
        self.value3_str = ctk.StringVar()
        self.slider3 = ctk.CTkSlider(self, from_=0, to=1, number_of_steps=6, variable=self.value3)
        self.slider3_label = ctk.CTkLabel(self, textvariable=self.value3_str)
        self.slider3.place(relx=0.5, rely=0.81, anchor="center")
        self.slider3_label.place(relx=0.5, rely=0.875, anchor="center")

        self.var_int_to_string()
        self.toplevel_window = None

    def definition(self, value):
        # CTkMessagebox(title="Définition", message=f"{value.definition}", icon="Images/info_empty.png")
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = DefinitionWindow(value)  # create window if its None or destroyed
            self.toplevel_window.grab_set()
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def var_int_to_string(self):
        #Pour l'affichage du slider, il semble plus comprehensible d'utiliser des indicateurs textuels,
        #plutot que les valeurs initiales comprises entre 0 et 1
        if self.value1.get() == 0.:
            self.value1_str.set("Très peu importante")
        if self.value1.get() == 0.16666666666666674:
            self.value1_str.set("Peu importante")
        if self.value1.get() == 0.33333333333333337:
            self.value1_str.set("Plutôt peu importante")
        if self.value1.get() == 0.5:
            self.value1_str.set("Importance modérée")
        if self.value1.get() == 0.6666666666666667:
            self.value1_str.set("Plutôt importante")
        if self.value1.get() == 0.8333333333333334:
            self.value1_str.set("Importante")
        if self.value1.get() == 1:
            self.value1_str.set("Très importante")

        if self.value2.get() == 0.:
            self.value2_str.set("Très peu importante")
        if self.value2.get() == 0.16666666666666674:
            self.value2_str.set("Peu importante")
        if self.value2.get() == 0.33333333333333337:
            self.value2_str.set("Plutôt peu importante")
        if self.value2.get() == 0.5:
            self.value2_str.set("Importance modérée")
        if self.value2.get() == 0.6666666666666667:
            self.value2_str.set("Plutôt importante")
        if self.value2.get() == 0.8333333333333334:
            self.value2_str.set("Importante")
        if self.value2.get() == 1:
            self.value2_str.set("Très importante")

        if self.value3.get() == 0.:
            self.value3_str.set("Très peu importante")
        if self.value3.get() == 0.16666666666666674:
            self.value3_str.set("Peu importante")
        if self.value3.get() == 0.33333333333333337:
            self.value3_str.set("Plutôt peu importante")
        if self.value3.get() == 0.5:
            self.value3_str.set("Importance modérée")
        if self.value3.get() == 0.6666666666666667:
            self.value3_str.set("Plutôt importante")
        if self.value3.get() == 0.8333333333333334:
            self.value3_str.set("Importante")
        if self.value3.get() == 1:
            self.value3_str.set("Très importante")
        #On appelle la fonction tous les 200ms
        self.after(200, self.var_int_to_string)



if __name__ == "__main__":
    values, values_name_only, situation_list = read_values_and_situations("data/values.csv", "data/situations.csv")
    app = SlidersGUI(values, values)
    app.mainloop()

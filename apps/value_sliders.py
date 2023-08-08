import customtkinter as ctk
import numpy as np
from PIL import Image
from utils.data import read_values_and_situations, Value
from typing import List


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

class ValuesSliders(ctk.CTk):

    def __init__(self, values : List[Value]):
        super().__init__()
        self.iconbitmap('Images/liris.ico')
        self.title("Questionnaire valeurs")
        self.geometry("900x700")

        self.values = values

        self.title_label = ctk.CTkLabel(self, text="Quelles valeurs sont importantes pour vous ?", font=ctk.CTkFont(size=22, weight="bold"))
        self.title_label.place(relx=0.5, rely=0.06, anchor="center")
        self.first_frame = ValuesFrame(self, 0.25, 0.5, self.values[0], self.values[1], self.values[2])
        self.second_frame = ValuesFrame(self, 0.75, 0.5, self.values[3], self.values[4], self.values[5])
        self.button = ctk.CTkButton(self, text="Confirmer", command=self.save)
        self.button.place(relx = 0.5, rely=0.95, anchor = "center")

        #self.results = np.zeros(len(self.values))
        self.results = []

    def save(self):
        # self.results[0] = self.first_frame.value1.get()
        # self.results[1] = self.first_frame.value2.get()
        # self.results[2] = self.first_frame.value3.get()
        # self.results[3] = self.second_frame.value1.get()
        # self.results[4] = self.second_frame.value2.get()
        # self.results[5] = self.second_frame.value3.get()
        self.results.append(self.first_frame.value1.get())
        self.results.append(self.first_frame.value2.get())
        self.results.append(self.first_frame.value3.get())
        self.results.append(self.second_frame.value1.get())
        self.results.append(self.second_frame.value2.get())
        self.results.append(self.second_frame.value3.get())
        print(self.results)
        self.destroy()    

class ValuesFrame(ctk.CTkFrame):
    def __init__(self, parent: ValuesSliders,_relx, _rely, value1 : Value, value2 : Value, value3 : Value):
        super().__init__(master=parent)
        self.info_img = ctk.CTkImage(Image.open("Images/q.png"), size=(30,30))
        self.place(relx = _relx, rely= _rely, relwidth = 0.48, relheight = 0.75, anchor="center")
        self.font = ctk.CTkFont(size=16, weight="bold")
        self.font2 = ctk.CTkFont(size=12)

        self.value1_title = ctk.CTkLabel(master=self, text=value1.name_fr, font=self.font)
        self.value1_title.place(relx= 0.5, rely=0.12, anchor="center")
        self.value1_definition = ctk.CTkLabel(master=self, text=value1.definition_fr, font=self.font2)
        self.value1_definition.place(relx= 0.5, rely=0.18, anchor="center")
        self.value1 = ctk.DoubleVar(value=0.5)
        self.value1_str = ctk.StringVar()
        self.slider1 = ctk.CTkSlider(self, width = 300, from_=0, to=1, number_of_steps=6, variable=self.value1)
        self.slider1_label = ctk.CTkLabel(self, textvariable=self.value1_str)
        self.slider1.place(relx=0.5, rely=0.23, anchor="center")
        self.slider1_label.place(relx=0.5, rely=0.28, anchor="center")

        self.value2_title = ctk.CTkLabel(master=self, text=value2.name_fr, font=self.font)
        self.value2_title.place(relx= 0.5, rely=0.42, anchor="center")
        self.value2_definition = ctk.CTkLabel(master=self, text=value2.definition_fr, font=self.font2)
        self.value2_definition.place(relx= 0.5, rely=0.48, anchor="center")
        self.value2 = ctk.DoubleVar(value=0.5)
        self.value2_str = ctk.StringVar()
        self.slider2 = ctk.CTkSlider(self, width = 300, from_=0, to=1, number_of_steps=6, variable=self.value2)
        self.slider2_label = ctk.CTkLabel(self, textvariable=self.value2_str)
        self.slider2.place(relx=0.5, rely=0.53, anchor="center")
        self.slider2_label.place(relx=0.5, rely=0.58, anchor="center")

        self.value3_title = ctk.CTkLabel(master=self, text=value3.name_fr, font=self.font)
        self.value3_title.place(relx= 0.5, rely=0.72, anchor="center")
        self.value3_definition = ctk.CTkLabel(master=self, text=value3.definition_fr, font=self.font2)
        self.value3_definition.place(relx= 0.5, rely=0.78, anchor="center")
        self.value3 = ctk.DoubleVar(value=0.5)
        self.value3_str = ctk.StringVar()
        self.slider3 = ctk.CTkSlider(self, width=300, from_=0, to=1, number_of_steps=6, variable=self.value3)
        self.slider3_label = ctk.CTkLabel(self, textvariable=self.value3_str)
        self.slider3.place(relx=0.5, rely=0.83, anchor="center")
        self.slider3_label.place(relx=0.5, rely=0.88, anchor="center")

        self.var_int_to_string()
        self.toplevel_window = None

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
    app = ValuesSliders(values)
    app.mainloop()

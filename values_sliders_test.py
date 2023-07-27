import customtkinter as ctk
import numpy as np
from data import store, read_values_and_situations
from PIL import Image
from situation import Value
from CTkMessagebox import CTkMessagebox
from typing import List


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

class ValuesSliders(ctk.CTk):

    def __init__(self, list_values : List[Value]):
        super().__init__()
        self.iconbitmap('Images/liris.ico')
        self.title("Questionnaire valeurs")
        self.geometry(f"{500}x{150+75*len(list_values)}")
        self.list_values = list_values

        self.title_label = ctk.CTkLabel(self, text="Quelles valeurs sont importantes pour vous ?", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")
        self.main_frame = MainFrame(self)
        self.button = ctk.CTkButton(self, text="Confirmer", command=self.save)
        self.button.place(relx = 0.5, rely=0.9, anchor = "center")

    def save(self):


        self.destroy()    

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent: ValuesSliders):
        super().__init__(master=parent)
        self.place(relx=0.02, rely=0.2, relwidth = 0.96, relheight = 0.65)
        self.info_img = ctk.CTkImage(Image.open("Images/info_empty.png"), size=(30,30))

        if len(parent.list_values) == 2 :

            self.value1_importance = ctk.IntVar()
            self.value1_importance_str = ctk.StringVar()
            value1_name = ctk.CTkLabel(master=self, text=f"{parent.list_values[0]}")
            value1_slider = ctk.CTkSlider(self, from_=0, to=6, number_of_steps=6, variable = self.value1_importance)
            value1_slider_label = ctk.CTkLabel(self, textvariable=self.value1_importance_str)
            self.value1_def_button = ctk.CTkButton(master=self, width=30, text="", 
                                                   fg_color = "transparent", image=self.info_img, 
                                                   command = lambda: self.definition(parent.list_values[0]))

            self.value2_importance = ctk.IntVar()
            self.value2_importance_str = ctk.StringVar()
            value2_name = ctk.CTkLabel(master=self, text=f"{parent.list_values[1]}")
            value2_slider = ctk.CTkSlider(self, from_=0, to=6, number_of_steps=6, variable = self.value2_importance)
            value2_slider_label = ctk.CTkLabel(self, textvariable=self.value2_importance_str)
            self.value2_def_button = ctk.CTkButton(master=self, width=30, text="", 
                                                   fg_color = "transparent", image=self.info_img, 
                                                   command = lambda: self.definition(parent.list_values[1]))
        
        if len(parent.list_values) == 3 :

            self.value1_importance = ctk.IntVar()
            self.value1_importance_str = ctk.StringVar()
            value1_name = ctk.CTkLabel(master=self, text=f"{parent.list_values[0]}")
            value1_slider = ctk.CTkSlider(self, from_=0, to=6, number_of_steps=6, variable = self.value1_importance)
            value1_slider_label = ctk.CTkLabel(self, textvariable=self.value1_importance_str)
            self.value1_def_button = ctk.CTkButton(master=self, width=30, text="", 
                                                   fg_color = "transparent", image=self.info_img, 
                                                   command = lambda: self.definition(parent.list_values[0]))

            self.value2_importance = ctk.IntVar()
            self.value2_importance_str = ctk.StringVar()
            value2_name = ctk.CTkLabel(master=self, text=f"{parent.list_values[1]}")
            value2_slider = ctk.CTkSlider(self, from_=0, to=6, number_of_steps=6, variable = self.value2_importance)
            value2_slider_label = ctk.CTkLabel(self, textvariable=self.value2_importance_str)
            self.value2_def_button = ctk.CTkButton(master=self, width=30, text="", 
                                                   fg_color = "transparent", image=self.info_img, 
                                                   command = lambda: self.definition(parent.list_values[1]))

            self.value3_importance = ctk.IntVar()
            self.value3_importance_str = ctk.StringVar()
            value3_name = ctk.CTkLabel(master=self, text=f"{parent.list_values[2]}")
            value3_slider = ctk.CTkSlider(self, from_=0, to=6, number_of_steps=6, variable = self.value3_importance)
            value3_slider_label = ctk.CTkLabel(self, textvariable=self.value3_importance_str)
            self.value3_def_button = ctk.CTkButton(master=self, width=30, text="", 
                                                   fg_color = "transparent", image=self.info_img, 
                                                   command = lambda: self.definition(parent.list_values[2]))


        if len(parent.list_values) == 7 :

            self.value1_importance = ctk.IntVar()
            self.value1_importance_str = ctk.StringVar()
            self.value1_name = ctk.CTkLabel(master=self, text=f"{parent.list_values[0]}")
            self.value1_slider = ctk.CTkSlider(self, from_=0, to=6, number_of_steps=6, variable = self.value1_importance)
            self.value1_slider_label = ctk.CTkLabel(self, textvariable=self.value1_importance_str)
            self.value1_def_button = ctk.CTkButton(master=self, width=30, text="", 
                                                   fg_color = "transparent", image=self.info_img, 
                                                   command = lambda: self.definition(parent.list_values[0]))
            self.value1_name.place(relx=0.2, rely=0.1, anchor="w")
            self.value1_def_button.place(relx=0.1, rely=0.1, anchor="center")
            self.value1_slider.place(relx=0.3, rely=0.2, anchor="center")
            self.value1_slider_label.place(relx=0.3, rely=0.3, anchor="center")

            self.value2_importance = ctk.IntVar()
            self.value2_importance_str = ctk.StringVar()
            self.value2_name = ctk.CTkLabel(master=self, text=f"{parent.list_values[1]}")
            self.value2_slider = ctk.CTkSlider(self, from_=0, to=6, number_of_steps=6, variable = self.value2_importance)
            self.value2_slider_label = ctk.CTkLabel(self, textvariable=self.value2_importance_str)
            self.value2_def_button = ctk.CTkButton(master=self, width=30, text="", 
                                                   fg_color = "transparent", image=self.info_img, 
                                                   command = lambda: self.definition(parent.list_values[1]))

            self.value3_importance = ctk.IntVar()
            self.value3_importance_str = ctk.StringVar()
            self.value3_name = ctk.CTkLabel(master=self, text=f"{parent.list_values[2]}")
            self.value3_slider = ctk.CTkSlider(self, from_=0, to=6, number_of_steps=6, variable = self.value3_importance)
            self.value3_slider_label = ctk.CTkLabel(self, textvariable=self.value3_importance_str)
            self.value3_def_button = ctk.CTkButton(master=self, width=30, text="", 
                                                   fg_color = "transparent", image=self.info_img, 
                                                   command = lambda: self.definition(parent.list_values[2]))

            self.value4_importance = ctk.IntVar()
            self.value4_importance_str = ctk.StringVar()
            self.value4_name = ctk.CTkLabel(master=self, text=f"{parent.list_values[3]}")
            self.value4_slider = ctk.CTkSlider(self, from_=0, to=6, number_of_steps=6, variable = self.value4_importance)
            self.value4_slider_label = ctk.CTkLabel(self, textvariable=self.value4_importance_str)
            self.value4_def_button = ctk.CTkButton(master=self, width=30, text="", 
                                                   fg_color = "transparent", image=self.info_img, 
                                                   command = lambda: self.definition(parent.list_values[3]))
            
            self.value5_importance = ctk.IntVar()
            self.value5_importance_str = ctk.StringVar()
            self.value5_name = ctk.CTkLabel(master=self, text=f"{parent.list_values[4]}")
            self.value5_slider = ctk.CTkSlider(self, from_=0, to=6, number_of_steps=6, variable = self.value2_importance)
            self.value5_slider_label = ctk.CTkLabel(self, textvariable=self.value2_importance_str)
            self.value5_def_button = ctk.CTkButton(master=self, width=30, text="", 
                                                   fg_color = "transparent", image=self.info_img, 
                                                   command = lambda: self.definition(parent.list_values[4]))

            self.value6_importance = ctk.IntVar()
            self.value6_importance_str = ctk.StringVar()
            self.value6_name = ctk.CTkLabel(master=self, text=f"{parent.list_values[5]}")
            self.value6_slider = ctk.CTkSlider(self, from_=0, to=6, number_of_steps=6, variable = self.value3_importance)
            self.value6_slider_label = ctk.CTkLabel(self, textvariable=self.value3_importance_str)
            self.value6_def_button = ctk.CTkButton(master=self, width=30, text="", 
                                                   fg_color = "transparent", image=self.info_img, 
                                                   command = lambda: self.definition(parent.list_values[5]))

            self.value7_importance = ctk.IntVar()
            self.value7_importance_str = ctk.StringVar()
            self.value7_name = ctk.CTkLabel(master=self, text=f"{parent.list_values[6]}")
            self.value7_slider = ctk.CTkSlider(self, from_=0, to=6, number_of_steps=6, variable = self.value4_importance)
            self.value7_slider_label = ctk.CTkLabel(self, textvariable=self.value4_importance_str)
            self.value7_def_button = ctk.CTkButton(master=self, width=30, text="", 
                                                   fg_color = "transparent", image=self.info_img, 
                                                   command = lambda: self.definition(parent.list_values[6]))





    def definition(self, value):
        CTkMessagebox(title="Définition", message=value.definition, icon="Images/info_empty.png")

if __name__ == "__main__":
    values, values_name_only, situation_list = read_values_and_situations("data/values.csv", "data/situations.csv")
    app = ValuesSliders(values)
    app.mainloop()
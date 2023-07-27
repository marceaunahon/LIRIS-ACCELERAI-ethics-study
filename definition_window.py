from data import Value
import customtkinter as ctk

class DefinitionWindow(ctk.CTkToplevel):

    def __init__(self, value : Value, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.after(200, lambda: self.iconbitmap('Images/liris.ico'))
        self.geometry("500x100")
        self.title(f"Définition de la valeur {value.name_fr}")
        self.label = ctk.CTkLabel(self, text=f"{value.name_fr} : {value.definition}")
        self.label.place(relx=0.5, rely=0.3, anchor="center")
        self.attributes('-topmost', True)
        self.resizable(False, False)
        self.button = ctk.CTkButton(master=self, text="Revenir au questionnaire", command=self.destroy)
        self.button.place(relx=0.5, rely=0.7, anchor="center")
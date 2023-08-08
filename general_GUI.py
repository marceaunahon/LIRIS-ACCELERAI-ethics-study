import customtkinter as ctk
from abc import ABC, abstractmethod
from CTkMessagebox import CTkMessagebox
from situation import Situation
from typing import List
import numpy as np

class GeneralGUI(ctk.CTk, ABC):
    
    def __init__(self, situation_list: List[Situation], title : str, size : List[int]):
        super().__init__()
        self.iconbitmap('Images/liris.ico')
        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")

        #Creation des listes
        self.situation_list = situation_list #la liste des situations
        self.situation_count = 0 #itérateur sur les situations
        self.situation = situation_list[self.situation_count] #la situation actuellement étudiée
        self.id = np.zeros(len(situation_list)) #liste des identifiants des situations


    @abstractmethod
    def save(self):
        pass

    def next(self):
        self.save()
        if self.situation_count < len(self.situation_list) - 1: #il reste des situations à traiter
            self.situation_count += 1
            self.situation = self.situation_list[self.situation_count] #on passe à la situation suivante
            self.reset() #on change l'image, le texte et les indicateurs, et on réinitialise les boutons et sliders à leur position d'origine
        else : #il n'y a plus de situations à traiter
            self.destroy()

    def previous(self):
        if self.situation_count == 0:
            #Si on est à la première situation, il faut afficher une erreur et rester sur la situation
            CTkMessagebox(title="Erreur",message="Vous êtes déjà à la première situation", icon="cancel")
        else : 
            self.situation_count -= 1 #l'itérateur sur les situations reprend sa valeur précédente
            self.situation = self.situation_list[self.situation_count] #on revient à la situation précédente
            self.reset()

    @abstractmethod
    def var_int_to_string(self):
        pass

    @abstractmethod
    def reset(self):
        pass


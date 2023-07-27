from data import read_values_and_situations, store
from menu import Menu
from questionnaire import Questionnaire
from sliders_GUI import SlidersGUI
from choice_situation_GUI import ChoiceSituationGUI
from acceptability_GUI import AcceptabilityGUI
from acceptability_GUI2 import AcceptabilityGUI2
from user import User
import numpy as np
from data import Value, ChoiceSituation


values, values_name_only, situation_list = read_values_and_situations("data/values.csv", "data/situations.csv")
menu = Menu(values, values_name_only, situation_list)
menu.mainloop()

profile = []
sliders_results = []
choice_results = []
acceptability_results = []
choice_results_list = []
acceptability_results_list = []

if menu.global_param[0] == 1:
    questionnaire = Questionnaire()
    questionnaire.mainloop()
    profile = questionnaire.results
if menu.global_param[1] == 1:
    if menu.sliders_param == 0:
        sliders = SlidersGUI(all_values=values, selected_values=values)
        sliders.mainloop()
        sliders_results = sliders.results
    if menu.sliders_param == 1:
        sliders = SlidersGUI(all_values=values, selected_values=menu.selected_values)
        sliders.mainloop()
        sliders_results = sliders.results
if menu.global_param[2] == 1:
    choice_GUI = ChoiceSituationGUI(menu.selected_situations, use_difficulty=menu.choice_param[0], 
                                    use_relevance=menu.choice_param[1], disp_values=menu.choice_param[2])
    choice_GUI.mainloop()
    choice_results_matrix = choice_GUI.results
    choice_results_list = choice_results_matrix.tolist()
if menu.global_param[3] == 1:
    acceptability_GUI = AcceptabilityGUI2(menu.selected_situations) #voir pour disp values
    acceptability_GUI.mainloop()
    acceptability_results_matrix = acceptability_GUI.results
    acceptability_results_list = acceptability_results_matrix.tolist()

user = User(menu = menu.list,
            profile = profile, 
            sliders_responses = sliders_results,
            choice_responses = choice_results_list,
            acceptability_responses = acceptability_results_list)
user.save()


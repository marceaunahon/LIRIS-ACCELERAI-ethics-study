from apps.utils.data_parser import read_values_and_situations, User
from apps.menu import Menu
from apps.questionnaire import Questionnaire
from apps.value_sliders import ValuesSliders
from apps.choice_situation import ChoiceSituationGUI
from apps.acceptability_situation import AcceptabilitySituationGUI
import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

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
    sliders = ValuesSliders(values)
    sliders.mainloop()
    sliders_results = sliders.results
if menu.global_param[2] == 1:
    choice_GUI = ChoiceSituationGUI(menu.selected_situations, use_difficulty=menu.choice_param[0], 
                                    use_relevance=menu.choice_param[1], disp_values=menu.choice_param[2])
    choice_GUI.mainloop()
    choice_results_matrix = choice_GUI.results
    choice_results_list = choice_results_matrix.tolist()
if menu.global_param[3] == 1:
    acceptability_GUI = AcceptabilitySituationGUI(menu.selected_situations) #voir pour disp values
    acceptability_GUI.mainloop()
    acceptability_results = acceptability_GUI.acceptabilities

# user = User(menu = menu.list,
#             profile = profile, 
#             sliders_responses = sliders_results,
#             choice_responses = choice_results_list,
#             acceptability_responses = acceptability_results_list)
# user.save()


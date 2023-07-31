# How it works

- In order to launch the app, you have to run the menu.py file. It will then launch a Menu instance, i.e. a GUI that asks you what application you want to launch, and to select params. There are four applications:
    - **Questionnaire** (*Questionnaire utilisateur*): an user questionnaire that allows to gather data about user profile
    - **SlidersGUI** (*Questionnaire valeurs*): presents all the values to the user and asks them to quantify their importance thanks to sliders
    - **ChoiceSituationGUI** (*Choix en situation*): presents a situation and two options, the user must choose one the two possibilites
        - You can show the user the value that corresponds which corresponds to each option (*Montrer les valeurs*)
        - You can ask the user to quantify how hard it is to decide with a slider (*Demander la difficulté*)
        - You can ask the user to quantify the relevance of the situation (*Demander la pertinence*)
    - **AcceptabilityGUI** (*Acceptabilité*): presents a situation and the option chosen by the system. Ask the user to judge the option and decide if he should let the system act or intervene
- A paramater (*Nombre de situations*) allows to choose how many situations will be presented for each couple of values in the ChoiceSituationGUI and AcceptabilityGUI
- The menu also asks what value you want to study
- The results and data processing are in the nooteboks


# Modules

- The applications are implemented with the module **customtkinter** (ctk), an extension of the module **tkinter**, you can find information on the following two links:
    - https://github.com/TomSchimansky/CustomTkinter
    - https://customtkinter.tomschimansky.com/
- Are also used:
    - **CTkMessagebox** and the class **CTkMessagebox**: little additional ctk windows
    - **pandas** to manage data from the .csv files
    - **numpy** mainly to create lists
    - **PIL** and the module **Image** to use images in the GUIs
    - **typing** and the variable **List** to make the code more readable
    - **abc** and the class **ABC** and function **abstractmethod** to create an abstract class


# Architecture

- Two .csv input files:
    - **values.csv**: contains all the values in the following format: Name;Name_fr;Definition_fr
    - **situations.csv**: contains all the situations in the following format: Id;Value1;Value2;Situation;Action1;Action2;Situation(acceptability);PathImage1;PathImage2

- Three .py files to manage data from the input files:
    - **value.py**: contains the class Value
    - **situation.py**: contains the class Situation
    - **data.py**: parse the two csv files and create Value and Situation instances

- Six apps .py files :
    - **general_GUI.py**: contains the abstract GUI class GeneralGUI
        - **choice_situations_GUI.py**: contains the GUI class ChoiceSituationGUI that inherites from GeneralGUI
        - **acceptability_GUI.py**: contains the GUI class AcceptabilityGUI that inherites from GeneralGUI
    - **questionnaire.py**: contains the GUI class Questionnaire
    - **sliders_GUI.py**: contains the GUI class SlidersGUI
    - **menu.py**: contains the GUI class Menu, enable to choose what application to launch

- One .py file to manage data from the Menu file:
    - **user.py**: contains the class User

- One .csv output file:
    - **results.csv**: contains all the results from the User instance created in menu.py

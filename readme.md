# Capturing stakeholders values and preferences regarding algorithmic systems

**Paper:** [Capturing stakeholders values and preferences regarding algorithmic systems](https://hal.science/hal-04487320v1/file/mNahon_ihm24.pdf)

**Authors:** Marceau Nahon, Aurélien Tabard, Audrey Serna

**Contact:** marceau.nahon@gmail.com

In this paper, we investigate how users’ preferences can be captured in order to incorporate more ethical considerations in the design of such systems. Adopting a value sensitive design approach, we propose a method to measure how much the context can impact the differences between the declared importance of values and decisions made in a given situation. We developed a survey tool that enable to measure importance of values in either absolute or relative ways, comparing pairs of values in specific situations. We conducted a preliminary study to test our survey tool with fifteen participants in the context of Smart Grids. Our results show differences in the way participants estimate values and underline the interest of capturing users preferences in context.

```bibtex
@inproceedings{nahon:hal-04487320,
  TITLE = {{Capturing stakeholders values and preferences regarding algorithmic systems}},
  AUTHOR = {Nahon, Marceau and Tabard, Aur{\'e}lien and Serna, Audrey},
  URL = {https://hal.science/hal-04487320},
  BOOKTITLE = {{IHM'24 - 35e Conf{\'e}rence Internationale Francophone sur l'Interaction Humain-Machine}},
  ADDRESS = {Paris, France},
  ORGANIZATION = {{AFIHM and Sorbonne Universit{\'e}}},
  HAL_LOCAL_REFERENCE = {TeC},
  VOLUME = {IHM'24 : Actes {\'e}tendus de la 35{\`e}me conf{\'e}rence Francophone sur l'Interaction Humain-Machine},
  YEAR = {2024},
  MONTH = Mar,
  KEYWORDS = {Value Sensitive Design ; Ethics ; Artificial Intelligence ; Smart-grids ; Survey tool ; Design sensible aux valeurs ; Ethique ; Intelligence Artificielle ; Smart-grids ; Outil d'enqu{\^e}te},
  PDF = {https://hal.science/hal-04487320/file/mNahon_ihm24.pdf},
  HAL_ID = {hal-04487320},
  HAL_VERSION = {v1},
}
```


## Install

```bash
>> python -m pip install -r requirements.txt
```
The applications are implemented with the module **customtkinter** (ctk), an extension of the module **tkinter**, you can find information on the following two links:  
    - https://github.com/TomSchimansky/CustomTkinter  
    - https://customtkinter.tomschimansky.com/


## Launch

- In order to launch the app, you have to run ``main.py``. It will then launch a Menu instance, i.e. a GUI that asks you what application you want to launch, and to select parameters. There are four applications:
    - **Questionnaire** (*Questionnaire utilisateur*): an user questionnaire that allows to gather data about user profile.
    - **ValuesSliders** (*Questionnaire valeurs*): presents all the values to the user and asks them to quantify their importance thanks to sliders.
    - **ChoiceSituationGUI** (*Choix en situation*): presents a situation and two options, the user must choose one of the two possibilites.
        - You can show the user the value that corresponds which corresponds to each option (*Montrer les valeurs*).
        - You can ask the user to quantify how hard it is to decide with a slider (*Demander la difficulté*).
        - You can ask the user to quantify the relevance of the situation (*Demander la pertinence*).
    - **AcceptabilitySituationGUI** (*Acceptabilité*): presents a situation and the option chosen by the system. Ask the user to judge the option and decide if he should let the system act or intervene.
- The parameter *Nombre de situations* allows to choose how many situations will be presented for each couple of values in the ChoiceSituationGUI and AcceptabilitySituationGUI.
- The menu also asks what value you want to study.
- The results and data processing are in the nootebok ``result_analysis.ipynb``.


## Supplementary material
 
This [google drive link](https://docs.google.com/spreadsheets/d/1Tqz-7S0gbLO5fKInpwF88NEyRvWMSgn35qGMMRKGPbw/edit?usp=sharing) gives access to:
- all the values, their source and definition.
- our categorisation.
- all the situations.

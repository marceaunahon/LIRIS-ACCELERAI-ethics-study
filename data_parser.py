import pandas as pd
from typing import List, Any
from value import Value
from situation import Situation
from user import User

def read_values_and_situations(filename_values : str, filename_situations : str):
    #filename_values : nom du fichier csv contenant les valeurs au format suivant : Name;Name_fr;Definition_fr
    #filename_dilemmas : nom du fichier csv contenant les dilemmes au format suivant : Id;Value1;Value2;Situation;Action1;Action2;Situation(acceptability);PathImage1;PathImage2
    values = [] #liste vide qui contiendra toutes les valeurs du fichier csv
    values_name_only = [] #liste vide qui contiendra uniquement les noms des valeurs 
    choice_situations = [] #liste vide qui contiendra les dilemmes 
    df_values = pd.read_csv(filename_values, sep=";", encoding='utf-8') #on lit le fichier csv des valeurs avec pandas
    df_situations = pd.read_csv(filename_situations, sep=";", encoding='utf-8') #on lit le fichier csv des dilemmes avec pandas
    for index, rowV in df_values.iterrows(): #on itère sur le dataframe des valeurs
        values.append(Value(rowV[0], rowV[1], rowV[2])) #on créé les valeurs et on les ajoute à la liste values
    values_name_only = df_values.iloc[:,0].tolist() #on extrait la première colonne du dataframe des valeurs et on la convertit en liste    
    for index, rowS in df_situations.iterrows(): #on itère sur le dataframe des dilemmes
        choice_situations.append(Situation(rowS[0], values[values_name_only.index(rowS[1])], values[values_name_only.index(rowS[2])], 
                rowS[3], rowS[4], rowS[5], rowS[6], rowS[7], rowS[8]))#on créé les situations et on les ajoute à la liste des situations
    return values, values_name_only, choice_situations

def read_user(filename_user : str):
    #filename_user : nom du fichier csv contenant les utilisateurs au format suivant : Id;Time;Param;Profile;Sliders_responses;Choice_responses;Acceptability_responses
    users = [] #liste vide qui contiendra tous les utilisateurs du fichier csv
    df_user = pd.read_csv(filename_user,  sep=";", encoding='utf-8') #on lit le fichier csv avec pandas
    for index, rowU in df_user.iterrows(): #on itère sur la dataframe des utilisateurs
        users.append(User(rowU[0], rowU[1], rowU[2], rowU[3], rowU[4], rowU[5], rowU[6])) #on crée les utilisateurs et on les ajoute à la liste users
    return users
        

def store(filename, name1, list1, name2 = None, list2 = None, 
          name3 = None, list3 = None, name4 = None, list4 = None,
          name5 = None, list5 = None, name6 = None, list6 = None):
    #Permet de stocker de une à six listes dans un fichier csv

    dict = {name1 : list1, name2 : list2, name3 : list3, name4 : list4, name5 : list5, name6 : list6}
    df = pd.DataFrame(dict)
    df.to_csv(filename)


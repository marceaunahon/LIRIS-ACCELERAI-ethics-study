from typing import List
import numpy as np
from apps.utils.data_parser import Situation, Value

class PairwiseComparison():

    def __init__(self, values : List[Value]):
        self.values = values #une PairwiseComparison de valeurs a une liste de valeurs à comparer
        self.size = (len(values),len(values)) #taille des matrices de comparaison
        self.raw_matrix = np.zeros(self.size) #première matrice: ne prend pas en compte la difficulté (1 pour la gagnante, 0 pour la perdante)
        self.probability_matrix = np.zeros(self.size) #prend en compte la difficulté : la somme des scores vaut 1
        self.multiplicative_matrix = np.zeros(self.size) #prend en compte la difficulté : le produit des scores vaut 1

    def get_raw(self, choice_situations : List[Situation], choices : List[int]):
        for i in range(len(self.values)):
            value1 = self.values[i] #on trouve la première valeur
            for j in range(len(self.values)):
                value2 = self.values[j] #on trouve la deuxième valeur
                if i == j : self.raw_matrix[i][j] = 1
                for k in range(len(choice_situations)) :
                    #On met 1 dans la case de la confrontation correspondant à la valeur gagnante
                    #On met 0 dans la case de la confrontation correspondant à la valeur perdante
                    #La somme des deux cases correspondant à une même confrontation vaut 1
                    if (choice_situations[k].value1 == value1 and choice_situations[k].value2 == value2):
                        if choices[k] == 1. : self.raw_matrix[j][i] = 1
                        if choices[k] == 0. : self.raw_matrix[i][j] = 1
                    if (choice_situations[k].value1 == value2 and choice_situations[k].value2 == value1):
                        if choices[k] == 1. : self.raw_matrix[i][j] = 1
                        if choices[k] == 0. : self.raw_matrix[j][i] = 1
        return self.raw_matrix

    def get_probability(self, choice_situations : List[Situation], choices : List[int], weights : List[float]):
        for i in range(len(self.values)):
            value1 = self.values[i] #on trouve la première valeur
            for j in range(len(self.values)):
                value2 = self.values[j] #on trouve la deuxième valeur
                if i == j : self.probability_matrix[i][j] = 1 #les diagonales prennent 1
                for k in range(len(choice_situations)) :
                    #Les deux valeurs partent avec un score égal (50%-50%)
                    #On ajoute à la valeur gagnante le poids qui correspond à sa victoire 
                    #(plus la difficulté de décision est faible plus le poids est élevé)
                    #On soustrait à la valeur perdante le poids qui correspond à sa défaite (même poids)
                    #La somme des deux cases correspondant à une même confrontation vaut 1
                    if (choice_situations[k].value1 == value1 and choice_situations[k].value2 == value2):
                        if choices[k] == 0. :
                            self.probability_matrix[i][j] = 0.5 + weights[k]
                            self.probability_matrix[j][i] = 0.5 - weights[k]
                        if choices[k] == 1. :
                            self.probability_matrix[j][i] = 0.5 + weights[k]
                            self.probability_matrix[i][j] = 0.5 - weights[k]
                    if (choice_situations[k].value1 == value2 and choice_situations[k].value2 == value1):
                        if choices[k] == 0. :
                            self.probability_matrix[j][i] = 0.5 + weights[k]
                            self.probability_matrix[i][j] = 0.5 - weights[k]
                        if choices[k] == 1. :
                            self.probability_matrix[i][j] = 0.5 + weights[k]
                            self.probability_matrix[j][i] = 0.5 - weights[k]
        return self.probability_matrix

    def get_multiplicative(self):
        for i in range(self.size[0]):
            for j in range(self.size[0]):
                if self.probability_matrix[i][j] == 1. and i != j:
                    #On considère que dans le cas ou une valeur à 1 dans la matrice de probabilty, 
                    # elle est 100 fois plus importante que celle qui lui est opposée
                    self.multiplicative_matrix[i][j] = 100
                    self.multiplicative_matrix[j][i] = 0.01
                else :
                    #Le produit des deux cases correspondant à une même confrontation vaut 1
                    self.multiplicative_matrix[i][j] = self.probability_matrix[i][j]/self.probability_matrix[j][i]
        return self.multiplicative_matrix
    
    def matrix_to_additive_score(self, values_name_only : List[str], matrix : str):
        #le score ici calculé est la somme des scores obtenu
        #matrix correspond à la matrice dont on veut calculer le score
        scores = np.zeros(len(values_name_only))
        dict1 = dict(zip(values_name_only, scores))
        valid = ["raw", "probability", "multiplicative"] #liste des matrices
        if not matrix in valid:
            #On s'assure que la matrice demandée existe bel et bien
            print('Veuillez choisir une matrice valide (raw, probability, multiplicative)')
            matrix = input("De quelle matrice voulez vous calculer le score?")
            self.matrix_to_additive_score(values_name_only, matrix)
        for i in range(len(values_name_only)):
            #On calcule le score en fonction de la matrice demandée
            if matrix == "raw" :
                dict1[values_name_only[i]] = np.sum(self.raw_matrix[i])
            if matrix == "probability" :
                dict1[values_name_only[i]] = np.sum(self.probability_matrix[i])
            if matrix == "multiplicative" :
                dict1[values_name_only[i]] = np.sum(self.multiplicative_matrix[i])
        dict2 = sorted (dict1.items (), key=lambda item: item [1], reverse=True)
        return dict2
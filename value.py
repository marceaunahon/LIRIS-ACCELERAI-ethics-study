class Value():

    def __init__(self, name : str = "Value", name_fr : str = "Valeur", definition : str = "ValueDef"):
        self.name = name #nom de la valeur
        self.name_fr = name_fr #nom de la valeur en français (pour la présenter à l'utilisateur)
        self.definition = definition #définition de la valeur
        self.score = 0.
        self.difference = 0.

    def __str__ (self) :
        #Affichage des valeurs
        res = self.name
        return res
    
    def get_score(self):
        return self.score
    
    def get_difference(self):
        return self.difference
    
    def disp_score_and_diff(self):
        res = "Points : " + str(self.score) + ", Différence : " + str(self.difference)
        print(res)
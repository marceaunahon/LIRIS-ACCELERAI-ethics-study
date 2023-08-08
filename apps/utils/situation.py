from value import Value

class Situation():

    def __init__(self, id : str, value1 : Value, value2 : Value, 
                 choice_statement : str, option1 : str, option2 : str,
                 threshold_statement : str,
                 im1_path :str, im2_path : str):
        self.id = id #identifiant de la situation (nombre de 1 au nombre de situations), afin de la retrouver
        self.value1 = value1 #première valeur mise en tension dans la situation
        self.value2 = value2 #deuxième valeur mise en tension dans la situation
        self.choice_statement = choice_statement #énoncé descriptif de la situation en questionnaire de choix
        self.option1 = option1
        self.option2 = option2
        self.threshold_statement = threshold_statement #énoncé descirptif de la situation en questionnaire d'acceptabilité
        self.im1_path = im1_path #chemin de l'image représentant la première valeur
        self.im2_path = im2_path #chemin de l'image représentant la deuxième valeur

    def __str__(self):
        #Affichage de l'énoncé du dilemme
        res = f"{self.id}:{self.value1}/{self.value2}"
        return res
    
    def get_value1(self):
        return self.value1
    
    def get_value2(self):
        return self.value2
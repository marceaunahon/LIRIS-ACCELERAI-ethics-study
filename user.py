import uuid
import time
import pandas as pd
import ast
import numpy as np

class User():

    def __init__(self, id = uuid.uuid4(), time = time.ctime(), menu = [], profile = [], sliders_responses = [], choice_responses = [], acceptability_responses = []):
        self.id = id
        self.time = time
        self.param = menu
        self.profile = profile
        self.sliders_responses = sliders_responses
        self.choice_responses = choice_responses
        self.acceptability_responses = acceptability_responses
        self.results = []

    def __str__(self):
        return str(self.id)
    
    def set_choices_responses(self):
        self.ids = []
        self.choices = []
        self.difficulties = []
        self.relevances = []
        self.choice_responses = ast.literal_eval(self.choice_responses)
        for i in range(len(self.choice_responses)):
            self.ids.append(float(self.choice_responses[i][0]))
            self.choices.append(float(self.choice_responses[i][1]))
            self.difficulties.append(float(self.choice_responses[i][2]))
            self.relevances.append(float(self.choice_responses[i][3]))
        
    def set_sliders_responses(self):
        self.sliders_responses = [i/(np.sum(ast.literal_eval(self.sliders_responses))) for i in ast.literal_eval(self.sliders_responses)]

    def save(self):
        self.results.append(self.id)
        self.results.append(self.time)
        self.results.append(self.param)
        self.results.append(self.profile)
        self.results.append(self.sliders_responses)
        self.results.append(self.choice_responses)
        self.results.append(self.acceptability_responses)
        df = pd.DataFrame([self.results])
        # Open the csv file in append mode and write the DataFrame to it
        with open("data/results.csv", "a") as f:
            df.to_csv(f, sep=";", index=False, header=False)
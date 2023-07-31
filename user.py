from data import store
import uuid
import time
import pandas as pd
import numpy as np

class User():

    def __init__(self, menu = [], profile = [], sliders_responses = [], choice_responses = [], acceptability_responses = []):
        self.id = uuid.uuid4()
        self.time = time.ctime()
        self.param = menu
        self.profile = profile
        self.sliders_responses = sliders_responses
        self.choice_responses = choice_responses
        self.acceptability_responses = acceptability_responses
        self.results = []
        

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
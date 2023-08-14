from typing import List
import ast

class Question():

    def __init__(self, title : str, answers_list : List[str]):
        self.title = title
        self.answers_list = ast.literal_eval(answers_list)

    def disp_question(self):
        print(f"Question: {self.title}")
        print("Answers:")
        for answer in self.answers_list :
            print(f"    {answer}")

    def __str__(self):
        return self.title
    
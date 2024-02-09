import random
import os

class Predictor:

    def predict_age(min_age, max_age):
        age = random.randint(int(min_age), int(max_age))
        print("Your age is.. " + str(age) + !")
        return age
    
    def predict_nationality(nationalities: list[str]):
        index = random.randint(0, len(nationalities))
        print("Your nationality is.. " + nationalities[index])
        return nationalities[index]
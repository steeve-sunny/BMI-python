import pandas as pd

class BMI(object):
    # initializing our parameters
    def __init__(self, name=None, height=None, weight=None):
        self.name = name
        self.weight = weight
        self.height = height

    # function calculates your BMI, with coditions based on criteria
    def BMI_Calculator(self):
        body_mass_index = self.weight / self.height ** 2

        if body_mass_index < 18.5:
            return f"{self.name} Your UnderWeight"

        elif body_mass_index >= 18.5 and body_mass_index < 25.0:
            return f"{self.name} Your Healthy Weight"

        elif body_mass_index >= 25.0 and body_mass_index < 30.0:
            return f"{self.name} Your OverWeight"
        
        else:
            return f"{self.name} Your Obese"



#b = BMI("steeve", 1.75, 67.5)
#print(b.BMI_Calculator())

# read data from a csv file and optimize the project
df = pd.read_csv("Data.csv")

# feeding in all rows to the BMI calculator at once 
for index, row in df.iterrows():
    b = BMI(row["name"], row["height_cm"], row["weight_kg"])
    print(b.BMI_Calculator())
   
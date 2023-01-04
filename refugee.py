import pandas
import os


class Refugee:
    if os.path.exists("refugees.csv"):
        refugees = pandas.read_csv("refugees.csv")
    else:
        refugees = pandas.DataFrame()

    def __init__(self, firstName, lastName, camp, condition, dependants):
        self.firstName = firstName
        self.lastName = lastName
        self.camp = camp
        self.condition = condition  # this could be a dictionary citing specific conditions
        self.dependants = dependants

        refugee = {"firstName": self.firstName, "lastName": self.lastName, "camp": self.camp,
                   "condition": self.condition, "dependants": self.dependants}
        df = pandas.DataFrame([refugee])
        Refugee.refugees = pandas.concat([Refugee.refugees, df], ignore_index=True)
        Refugee.refugees.to_csv("refugees.csv", index=False)

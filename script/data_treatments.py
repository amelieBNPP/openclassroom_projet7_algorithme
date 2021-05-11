import pandas as pd
import csv
import os

class TreatData:

    @staticmethod
    def read_file(file_name):
        colnames = ['share_name', 'share_price', 'share_return']
        data  = pd.read_csv(f"./data/{file_name}", names = colnames, header=0)
        return data

    @staticmethod
    def write_file(file_to_save, overwrite=True):
        if not os.path.exists("./solutions/brut_force.csv"):
            new_file = open("./solutions/brut_force.csv", 'x')
            new_file.close()
        writing_mode = 'w' if overwrite else 'a'
        with open("./solutions/brut_force.csv", writing_mode, newline='') as file:
            solution = csv.writer(file)#, lineterminator = ', ', quoting=csv.QUOTE_ALL)
            solution.writerows(file_to_save)
        print("save data in file: 0K")

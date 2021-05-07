import pandas as pd
import csv
import os

def read_file():
    colnames = ['share_name', 'share_price', 'share_return']
    data  = pd.read_csv("./data/Share_prices.csv", names = colnames, header=0)
    shares_detail = {
        'share_name': data['share_name'],
        'share_price': data['share_price'],
        'share_return': data['share_return']
    }
    return shares_detail

def write_file(file_to_save, overwrite=True):
    if not os.path.exists("./solutions/brut_force.csv"):
        new_file = open("./solutions/brut_force.csv", 'x')
        new_file.close()
    writing_mode = 'w' if overwrite else 'a'
    with open("./solutions/brut_force.csv", writing_mode, newline='') as file:
        solution = csv.writer(file)#, lineterminator = ', ', quoting=csv.QUOTE_ALL)
        solution.writerows(file_to_save)
    print("save data in file: 0K")

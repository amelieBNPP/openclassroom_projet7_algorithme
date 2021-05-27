## -*- coding: utf-8 -*-
"""
Created on Mar 31st
@author: Amelie Noury
"""
from script.data_treatments import TreatData
from controller.controller import Controller

def main():
    """ Main function :
    parameters : 
    - string value for data file name : "Share_prices.csv" OR "dataset1.csv" OR "dataset2.csv"
    - portfolio capacity : 500€ by default
    - optim_function : run_brut_force OR run_optim_pulp OR run_optim_scipy
    """

    file_name = "dataset2.csv"
    portfolio_capacity = 500
    optim_function = 'run_optim_pulp'

    controller_algo = Controller(file_name, portfolio_capacity, optim_function)
    controller_algo.run()

    # TreatData.data_describe(data)



 


main()

## -*- coding: utf-8 -*-
"""
Created on Mar 31st
@author: Amelie Noury
"""
from script.data_treatments import read_file, write_file
from script.timer import TimeToCompute
from script.brutforce import brutforce
import pandas as pd

def main():
    
    nb_share = 7
    data = read_file()
    input_share_name = data['share_name'][0:nb_share]
    input_data_prices = data['share_price'][0:nb_share]
    input_data_yield = pd.Series([
        float(dta.replace("%","")) for dta in data['share_return'][0:nb_share]
    ])

    portfolio_capacity = 500

    # brut_force with loops
    timer_brut_force = TimeToCompute()
    timer_brut_force.start()
    result_brut_force = brutforce(input_share_name, input_data_prices, input_data_yield, portfolio_capacity)
    timer_brut_force.end()

    print(f'--------------------SOLUTIONS-----------------------------')
 
    print(f'the brut force program with {len(input_share_name)} shares and a portfolio capacity of {portfolio_capacity} euros: ')
    print(result_brut_force)
    print(f'the brut force programme with itertools run during {timer_brut_force.time_pass()} sec \n')



main()

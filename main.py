## -*- coding: utf-8 -*-
"""
Created on Mar 31st
@author: Amelie Noury
"""
from script.data_treatments import TreatData
from script.timer import TimeToCompute
from script.brutforce import BrutForce
from script.optimized import optim

def main():
    
    run_brut_force = False
    run_optim_pulp = True
    run_optim_scipy = False

    data = TreatData.read_file("dataset2.csv")#("Share_prices.csv")#
    data = TreatData.remove_null_price(data)
    data = TreatData.remove_negative_price(data)
    nb_share = len(data) # 20
    input_share_name = data['share_name'][0:nb_share]
    input_data_prices = data['share_price'][0:nb_share]
    input_data_yield = data['share_return'][0:nb_share]

    portfolio_capacity = 500

    # brut_force with loops
    if run_brut_force:
        timer_brut_force = TimeToCompute()
        timer_brut_force.start()
        result_brut_force = BrutForce(input_share_name, input_data_prices, input_data_yield, portfolio_capacity)
        result_brut_force.brut_force()
        timer_brut_force.end()

    # optimize with pulp
    if run_optim_pulp:
        timer_optim_pulp = TimeToCompute()
        timer_optim_pulp.start()
        result_optim_pulp = optim(input_share_name, input_data_prices, input_data_yield, portfolio_capacity)
        result_optim_pulp.optimisation_by_pulp()
        timer_optim_pulp.end()

    # # optimize with scipy
    if run_optim_scipy:
        timer_optim_scipy = TimeToCompute()
        timer_optim_scipy.start()
        result_optim_scipy = optim(input_share_name, input_data_prices, input_data_yield, portfolio_capacity)
        result_optim_scipy.optimisation_with_scipy()
        timer_optim_scipy.end()


    print(f'--------------------SOLUTIONS-----------------------------')
 
    print(f'parameters :  {len(input_share_name)} shares and a portfolio capacity of {portfolio_capacity} euros: ')
    
    if run_brut_force:
        print('--BRUT FORCE--')
        print(result_brut_force)
        print(timer_brut_force.time_pass())

    if run_optim_pulp:
        print('--OPTIM PULP--')
        result_optim_pulp.show_optim()
        print(timer_optim_pulp.time_pass())

    if run_optim_scipy:
        print('--OPTIM SCIPY--')
        result_optim_scipy.show_optim()
        print(timer_optim_scipy.time_pass())



main()

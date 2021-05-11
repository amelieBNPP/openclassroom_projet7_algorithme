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
    
    nb_share = 20
    data = TreatData.read_file("Share_prices.csv")
    input_share_name = data['share_name'][0:nb_share]
    input_data_prices = data['share_price'][0:nb_share]
    input_data_yield = data['share_return'][0:nb_share]

    portfolio_capacity = 500

    # brut_force with loops
    timer_brut_force = TimeToCompute()
    timer_brut_force.start()
    result_brut_force = BrutForce(input_share_name, input_data_prices, input_data_yield, portfolio_capacity)
    result_brut_force.brut_force()
    timer_brut_force.end()

    # optimize with pulp
    timer_optim_pulp = TimeToCompute()
    timer_optim_pulp.start()
    result_optim_pulp = optim(input_share_name, input_data_prices, input_data_yield, portfolio_capacity)
    result_optim_pulp.optimisation_by_pulp()
    timer_optim_pulp.end()

    # # optimize with scipy
    timer_optim_scipy = TimeToCompute()
    timer_optim_scipy.start()
    result_optim_scipy = optim(input_share_name, input_data_prices, input_data_yield, portfolio_capacity)
    result_optim_scipy.optimisation_with_scipy()
    timer_optim_scipy.end()


    print(f'--------------------SOLUTIONS-----------------------------')
 
    print(f'parameters :  {len(input_share_name)} shares and a portfolio capacity of {portfolio_capacity} euros: ')
    
    print('--BRUT FORCE--')
    print(result_brut_force)
    print(timer_brut_force.time_pass())

    print('--OPTIM PULP--')
    result_optim_pulp.show_optim()
    print(timer_optim_pulp.time_pass())

    print('--OPTIM SCIPY--')
    result_optim_scipy.show_optim()
    print(timer_optim_scipy.time_pass())



main()

## -*- coding: utf-8 -*-
"""
Created on Mar 31st
@author: Amelie Noury
"""

def main():
    
    nb_share = 20
    data = read_file()
    input_share_name = data['share_name'][0:nb_share]
    input_data_prices = data['share_price'][0:nb_share]
    input_data_yield = [
        float(dta.replace("%","")) for dta in data['share_return'][0:nb_share]
    ]
    
    portfolio_capacity = 500


main()

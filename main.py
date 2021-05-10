## -*- coding: utf-8 -*-
"""
Created on Mar 31st
@author: Amelie Noury
"""
from pandas.core.frame import DataFrame
from script.data_treatments import read_file, write_file
import pandas as pd

def main():
    
    nb_share = 20
    data = read_file()
    input_share_name = DataFrame(data['share_name'][0:nb_share])
    input_data_prices = DataFrame(data['share_price'][0:nb_share])
    input_data_yield = DataFrame([
        float(dta.replace("%","")) for dta in data['share_return'][0:nb_share]
    ])
    
    portfolio_capacity = 500


main()

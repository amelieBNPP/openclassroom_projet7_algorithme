
from itertools import product
from operator import mul
import numpy as np

class BrutForce:
    def __init__(self, share_name, share_price, share_return, portfolio_capacity) -> None:
        self.share_name = share_name
        self.share_price = share_price
        self.share_return = share_return
        self.portfolio_capacity = portfolio_capacity

    def brut_force(self):
        """
        This function compute a brut force algorithm, that evaluates all possible combination of shares for
        a given number and price of shares with a constraint of amount invested in the portfolio.
        1. considere that the portfolio is compose of an unique share,
        find the maximum number of share so that the portfolio does not be above than the target
        2. compute all combinaison available using the itertools library
        3. compute all returns corresponding to the combinaison
        4. keep only the maximumreturn that correspond to the best solution
        """

        # 1. compute maximum
        nb_unknow = len(self.share_price)

        all_values = [[0, price] for price in self.share_price]

        # 2. compute all combinaison
        all_combinaisons = [combinaison for combinaison in product(*all_values) if sum(combinaison) <= self.portfolio_capacity]

        # 3. yields by share
        all_yields = [
            sum(map(mul, combinations, self.share_return))/100
            for combinations in all_combinaisons
        ]

        # 4. optimisation
        self.best_profit = {"Total Profit" : max(all_yields)}
        best_shares_index = all_yields.index(self.best_profit["Total Profit"])
        best_shares_list = all_combinaisons[best_shares_index]
        self.best_shares = {
            self.share_name[share_idx]: (best_combinaison / self.share_price[share_idx])
            for share_idx, best_combinaison in enumerate(best_shares_list) if best_combinaison != 0}

        self.best_cost = {"Best cost" : sum(best_shares_list)}

        return self.best_profit, self.best_shares, self.best_cost
 
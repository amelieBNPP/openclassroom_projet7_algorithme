import numpy as np
import pandas as pd
from scipy.optimize import minimize
from pulp import LpVariable, LpProblem, LpStatus, LpMaximize, lpSum, value


class Optim:
    def __init__(self, share_name, share_price, share_return, portfolio_capacity) -> None:
        self.share_name = share_name
        self.share_price = share_price
        self.share_return = share_return
        self.portfolio_capacity = portfolio_capacity

    def objective_function(self, x) -> float:
        solution = 0    
        for i in range(len(x)):
            solution += x[i] * self.share_return[i] 
        return -solution

    def constraint(self, x) -> float:
        portfolio_capacity = self.portfolio_capacity
        for i in range(len(x)):
            portfolio_capacity -= x[i] * self.share_price[i]
        return portfolio_capacity

    def optimisation_with_scipy(self):

        x0 = np.zeros(len(self.share_name))

        max_number_of_share = [self.portfolio_capacity//price for price in self.share_price]
        bnds = [(0,n+1) for n in max_number_of_share]

        con1 = {'type': 'ineq', 'fun':self.constraint}

        solution = minimize(self.objective_function, x0, method='SLSQP', \
            bounds=bnds, constraints=[con1])

        self.best_shares = {
            self.share_name[i] : round(solution.x[i],2)
            for i in range(len(solution.x)) if round(solution.x[i]) != 0
        }

        self.best_profit = {"Total Profit": round(-solution.fun,2)}
        self.best_cost = {"Best cost" : solution.x  * self.share_price}

        return self.best_profit, self.best_shares, self.best_cost 

    def optimisation_by_pulp(self):

        share_price_dic = dict(zip(self.share_name,self.share_price))
        share_return_dic = dict(zip(self.share_name, self.share_return))

        share_vars = LpVariable.dicts("share", self.share_name, lowBound=0, cat='Integer')

        # setup problem
        total_score = LpProblem("optimize_investment", LpMaximize)
 
        ## objective function
        total_score += lpSum([share_return_dic[idx] * share_vars[idx] for idx in share_vars])
        ## constraint
        total_score += lpSum([share_price_dic[idx] * share_vars[idx] for idx in share_vars]) <= self.portfolio_capacity

        # solve problem
        total_score.solve()
        # Check the status of the problem, can be use at each step of the optimisation
        print("Current Status: ", LpStatus[total_score.status]) 

        # print solution
        self.best_shares = {
            share.name : share.varValue
            for share in total_score.variables() if share.varValue != 0
        }

        cost_share = [
            share_price_dic[share.name.replace('share_','').replace('_','-')]*share.varValue
            for share in total_score.variables()
        ]

        self.best_profit = {"Total Profit": round(value(total_score.objective),2)}
        self.best_cost = {"Best cost" : round(sum(cost_share),2)}

        return self.best_profit, self.best_shares, self.best_cost


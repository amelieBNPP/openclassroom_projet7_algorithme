
class View:

    def __init__(
            self,
            input_share_name,
            portfolio_capacity,
            algorithm) -> None:
        self.input_share_name = input_share_name
        self.portfolio_capacity = portfolio_capacity
        self.algorithm = algorithm

    def display_results(
            self,
            optim_result,
            optim_time,
            nb_share_before_treatment):
        self.best_profit = optim_result[0]
        self.best_shares = optim_result[1]
        self.best_cost = optim_result[2]

        print(f'\n-----------------------------------------------------------')
        print(f'|                   SOLUTIONS                             |')
        print(f'-----------------------------------------------------------\n')

        print(
            f'parameters : \n - {nb_share_before_treatment} shares before treatments')
        print(f' - {len(self.input_share_name)} shares after treatments')
        print(f' - portfolio capacity of {self.portfolio_capacity} euros \n')

        print(f'optimizer : {self.algorithm.upper()} : \n')
        self.display_optim()
        print(f'\n => {optim_time}\n')

    def display_optim(self) -> None:
        print('portfolio profit : ' +
              str(self.best_profit['Total Profit']) +
              ' euros\n')
        print('investment :')
        for share in self.best_shares:
            print(' -' +
                  str(int(self.best_shares[share])) +
                  ' share(s) ' +
                  share)
        print('\ninvestment cost : ' +
              str(self.best_cost['Best cost']) + ' euros')

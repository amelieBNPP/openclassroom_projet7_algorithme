import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame

class Graph:

    @staticmethod
    def plot_cloud(prices, returns, optim_result=None) -> None:
        plt.plot(prices,returns,"ob", label="all shares")
        plt.ylabel('Return after 2years')
        plt.xlabel('Price')
        plt.title('Relation between price and return of shares')

        if optim_result is not None:
            plt.plot(optim_result['share_price'], optim_result['share_return'], "or", label = "optimized shares")
            plt.legend()
        plt.show()

    @staticmethod
    def plot_result(results, data) -> DataFrame:
        share_name = list(results.best_share.keys())
        share_name_clean= [name.replace('share_','').replace('_','-') for name in share_name]
        
        index_to_plot = [data.loc[data['share_name'] == share_clean].index[0] for share_clean in share_name_clean]
        return data.iloc[index_to_plot,:]

    @staticmethod
    def hard_plot_brut_force_time() -> None:
        time_nbShare = [0, 0, 0.01, 0.07, 0.4, 2.7, 60.85, 1404.85]
        nb_share = [1, 2, 3, 4, 5, 6, 7, 8]
       
        plt.plot(nb_share, time_nbShare, linestyle='solid')
        plt.ylabel('time to run program with portfoliocapacity of 500€ (sec)')
        plt.xlabel('number of shares')
        plt.title('Time to run the brut force program in relation with the number of shares')
        plt.show()

        portfolio_capacity = [10, 20, 30, 50, 80, 100, 150, 200, 300]
        time_ptfCapacity = [0, 0, 0.08, 51.43, ]
        plt.plot(nb_share, time_ptfCapacity, linestyle='solid')
        plt.ylabel('time to run program (sec)')
        plt.xlabel('number of shares')
        plt.title('Time to run the brut force program in relation with the number of shares')
        plt.show()

 

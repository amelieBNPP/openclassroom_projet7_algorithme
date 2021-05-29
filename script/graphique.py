import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame


class Graph:

    @staticmethod
    def plot_cloud(
            prices,
            returns,
            optim_result=None,
            optim_to_compare=None) -> None:
        plt.plot(prices, returns, "ob", label="all shares")
        plt.ylabel('Return after 2years in €')
        plt.xlabel('Price in €')
        plt.title('Relation between price and return of shares')

        if optim_result is not None:
            plt.plot(
                optim_result['share_price'],
                optim_result['share_return'],
                "or",
                label="Brut Force selection")  # optimized shares
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15))

        if optim_to_compare is not None:
            plt.plot(
                optim_to_compare['share_price'],
                optim_to_compare['share_return'],
                "xy",
                label="optimized shares of Sienna")
            plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15))

        plt.show()

    @staticmethod
    def plot_result(results, data) -> DataFrame:
        share_name = list(results[1].keys())
        share_name_clean = [
            name.replace(
                'share_',
                '').replace(
                '_',
                '-') for name in share_name]

        return Graph.find_share_in_data_file(share_name_clean, data)

    @staticmethod
    def find_share_in_data_file(share_list, data) -> DataFrame:
        index_to_plot = [data.loc[data['share_name'] ==
                                  share_name].index[0] for share_name in share_list]
        return data.iloc[index_to_plot, :]

    @staticmethod
    def hard_plot_brut_force_time() -> None:
        time_nbShare = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.01, 0.02,
                        0.04, 0.06, 0.11, 0.23, 0.45, 0.9, 1.79, 3.47, 5.96]
        nb_share = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

        plt.plot(nb_share, time_nbShare, linestyle='solid')
        plt.ylabel('time to run program with portfoliocapacity of 500€ (sec)')
        plt.xlabel('number of shares')
        plt.title(
            'Time to run the brut force program in relation with the number of shares')
        plt.show()

        time_nbShare = [
            0.05,
            0.15,
            0.06,
            0.46,
            0.36,
            0.17,
            0.23,
            0.28,
            0.21,
            0.21]
        nb_share = [100, 200, 300, 400, 500, 600, 700, 800, 900, 957]

        plt.plot(nb_share, time_nbShare, linestyle='solid')
        plt.ylabel('time to run program with portfoliocapacity of 500€ (sec)')
        plt.xlabel('number of shares')
        plt.title(
            'Time to run the optimized program in relation with the number of shares')
        plt.show()

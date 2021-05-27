from script.timer import TimeToCompute
from script.brutforce import BrutForce
from script.optimized import Optim
from script.graphique import Graph
from script.data_treatments import TreatData
from view.show_results import View

class Controller:
    """This controller runs the algorithms and call the view to display the results"""

    def __init__(self, file_name, portfolio_capacity, algorithm, nb_share=None):
        self.data = TreatData.read_file(file_name)
        self.nb_share_before_treatment = len(self.data)
        self.data = TreatData.remove_null_price(self.data)
        self.data = TreatData.remove_negative_price(self.data)

        self.nb_share = len(self.data) if nb_share is None else nb_share
        self.input_share_name = self.data['share_name'][0:nb_share]
        self.input_data_prices = self.data['share_price'][0:nb_share]
        self.input_data_yield = self.data['share_return'][0:nb_share]

        self.portfolio_capacity = portfolio_capacity
        self.algorithm = algorithm
        self.show_results = View(self.input_share_name, self.portfolio_capacity ,self.algorithm)
        

    def run(self):
        timer_optim = TimeToCompute()
        timer_optim.start()

        # brut_force with loops
        if self.algorithm == 'run_brut_force':
            result_brut_force = BrutForce(self.input_share_name, self.input_data_prices, self.input_data_yield, self.portfolio_capacity)
            self.optim_result = result_brut_force.brut_force()
            # Graph.hard_plot_brut_force_time()

        # optimize with pulp
        if self.algorithm == 'run_optim_pulp':
            result_optim_pulp = Optim(self.input_share_name, self.input_data_prices, self.input_data_yield, self.portfolio_capacity)
            self.optim_result = result_optim_pulp.optimisation_by_pulp()
    
        # optimize with scipy
        if self.algorithm == 'run_optim_scipy':
            result_optim_scipy = Optim(self.input_share_name, self.input_data_prices, self.input_data_yield, self.portfolio_capacity)
            self.optim_result = result_optim_scipy.optimisation_with_scipy()

        timer_optim.end()

        self.show_results.display_results(self.optim_result, timer_optim.time_pass(), self.nb_share_before_treatment)

        # result_to_plot = Graph.plot_result(result_optim_pulp, self.data)
        # Graph.plot_cloud(self.input_data_prices, self.input_data_yield, result_to_plot)
        # timer_optim_pulp.big_o(result_optim_pulp.optimisation_by_pulp(), self.data)


        

from time import time
from bigO import BigO

class TimeToCompute:
    """This class allow to test the speed of a function"""

    def start(self):
        self.begining = time()

    def end(self):
        self.ending = time()

    def time_pass(self):
        return f'programme run during {round(self.ending - self.begining,2)} secondes'

    @staticmethod
    def big_o(fun, dta):
        print(BigO.test(fun, dta))


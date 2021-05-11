from time import time

class TimeToCompute:

    def start(self):
        self.begining = time()

    def end(self):
        self.ending = time()

    def time_pass(self):
        return f'programme run during {round(self.ending - self.begining,2)} secondes'


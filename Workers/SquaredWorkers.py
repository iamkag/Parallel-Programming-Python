import threading


class SquaredWorkers(threading.Thread):
    def __init__(self, n, **kwargs):
        self._n = n
        super(SquaredWorkers, self).__init__(**kwargs) # Call the parent class constructor which is threading.Thread
        self.start() # Start the thread
    
    def _calc_square(self):
        sum_square = 0
        for n in range(self._n):
            sum_square += n**2
        print("Result: ", sum_square)
    
    # Overwrite the run method from the thread parent class
    def run(self): 
        self._calc_square()
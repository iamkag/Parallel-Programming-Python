import threading
import time

class SleepyWorkers(threading.Thread):
    def __init__(self, seconds, **kwargs):
        self._seconds = seconds
        super(SleepyWorkers, self).__init__(**kwargs)
        self.start()
    
    def _sleep_a_while(self):
        time.sleep(self._seconds)
    
    def run(self):
        self._sleep_a_while()
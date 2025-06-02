import time
from SleepyWorkers import SleepyWorkers
from SquaredWorkers import SquaredWorkers

def threads_joining():

    calc_start_time = time.time()

    current_workers = []
    for i in range(5):
        maxim_value = (i+1)*1000000
        t = SquaredWorkers( n = maxim_value)
        current_workers.append(t)

    for i in range(len(current_workers)):
        current_workers[i].join() # Blocks programm execution until the thread is done. Nothing is allowed to happend until that thread finishes.

    print("Calculate sum of squares took ", round(time.time() - calc_start_time,1), " seconds")
    
    current_workers = []
    sleep_time_start = time.time()
    for i in range(1,6 ):
        t = SleepyWorkers(seconds = i)
        current_workers.append(t)
    
    for i in range(len(current_workers)):
        current_workers[i].join()

    print("Sleeping for a while took ", round(time.time() - sleep_time_start,1), " seconds") # This will be 5 seconds, it is the maximum of the 5 threads


def daemon_threads():

    calc_start_time = time.time()

    current_workers = []
    for i in range(5):
        maxim_value = (i+1)*1000000
        t = SquaredWorkers( n = maxim_value, daemon = True)
        current_workers.append(t)

    for i in range(len(current_workers)):
        current_workers[i].join() # Blocks programm execution until the thread is done. Nothing is allowed to happend until that thread finishes.

    print("Calculate sum of squares took ", round(time.time() - calc_start_time,1), " seconds")
    
    current_workers = []
    sleep_time_start = time.time()
    for i in range(1,6 ):
        t = SleepyWorkers(seconds = i, daemon = True)
        current_workers.append(t)
    
    for i in range(len(current_workers)-2):
        current_workers[i].join()

    print("Sleeping for a while took ", round(time.time() - sleep_time_start,1), " seconds") # This will be 5 seconds, it is the maximum of the 5 threads

if __name__ == "__main__":
    threads_joining()
    print("############################################")
    daemon_threads()
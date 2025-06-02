import time
import threading

def calc_square(numbers):
    sum_square = 0
    for n in range(numbers):
        sum_square += n**2
    print("Result: ", sum_square)

def sleep_a_while(seconds):
    time.sleep(seconds)


def threads_joining():

    calc_start_time = time.time()

    current_thread = []
    for i in range(5):
        maxim_value = (i+1)*1000000
        t = threading.Thread(target=calc_square, args=(maxim_value,))
        # Initiate the threads
        t.start()
        current_thread.append(t)

    for i in range(len(current_thread)):
        current_thread[i].join() # Blocks programm execution until the thread is done. Nothing is allowed to happend until that thread finishes.

    print("Calculate sum of squares took ", round(time.time() - calc_start_time,1), " seconds")
    
    current_thread = []
    sleep_time_start = time.time()
    for i in range(1,6 ):
        t = threading.Thread(target=sleep_a_while, args=(i,))
        t.start()
        current_thread.append(t)
    
    for i in range(len(current_thread)):
        current_thread[i].join()

    print("Sleeping for a while took ", round(time.time() - sleep_time_start,1), " seconds") # This will be 5 seconds, it is the maximum of the 5 threads


def daemon_threads():

    calc_start_time = time.time()

    current_thread = []
    for i in range(5):
        maxim_value = (i+1)*1000000
        t = threading.Thread(target=calc_square, args=(maxim_value,), daemon=True)
        # Initiate the threads
        t.start()
        current_thread.append(t)

    for i in range(len(current_thread)):
        current_thread[i].join() # Blocks programm execution until the thread is done. Nothing is allowed to happend until that thread finishes.

    print("Calculate sum of squares took ", round(time.time() - calc_start_time,1), " seconds")
    
    current_thread = []
    sleep_time_start = time.time()
    for i in range(1,6 ):
        t = threading.Thread(target=sleep_a_while, args=(i,), daemon=True)
        t.start()
        # t.join() ->> Block the whole execution until this thread is done
        current_thread.append(t)
    
    for i in range(len(current_thread) -2 ):
        current_thread[i].join()

    print("Sleeping for a while took ", round(time.time() - sleep_time_start,1), " seconds") # This will be 3 seconds, it is the maximum of the 5 threads

if __name__ == "__main__":
    threads_joining()
    print("############################################")
    daemon_threads()
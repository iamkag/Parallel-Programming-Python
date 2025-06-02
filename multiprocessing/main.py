import time
from multiprocessing import Process # Use more than one core


def check_value_list(x, i, num_processes):
    max_number_of_checks = 10**8
    lower = int((max_number_of_checks/num_processes) * i)
    upper = int((i+1) * (max_number_of_checks/num_processes))
    for i in range(lower, upper):
        i in x

num_processes = 4
comparison_list = [1,2,3]

start_time = time.time()
processes = []
for i in range(num_processes):
    process = Process(target=check_value_list, args=(comparison_list, i , num_processes)) # Split this operation across multiple cores
    processes.append(process)

for thread in processes:
    thread.start()

for thread in processes:
    thread.join()

print(f"Time taken: {time.time() - start_time}")
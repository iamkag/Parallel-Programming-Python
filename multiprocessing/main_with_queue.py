import time
from multiprocessing import Process, Queue


def check_value_list(x, i, num_processes, queue):
    max_number_of_checks = 10**8
    lower = int((max_number_of_checks/num_processes) * i)
    upper = int((i+1) * (max_number_of_checks/num_processes))
    number_of_hits = 0
    for i in range(lower, upper):
        if i in x:
            number_of_hits += 1

    queue.put((lower, upper, number_of_hits))

def main():
    num_processes = 4
    comparison_list = [1,2,3]
    queue = Queue()
    start_time = time.time()
    processes = []
    for i in range(num_processes):
        process = Process(target=check_value_list, args=(comparison_list, i , num_processes, queue))
        processes.append(process)

    for p in processes:
        p.start()

    for p in processes:
        p.join()
    
    queue.put("DONE")

    while True:
        v = queue.get()
        if v == "DONE":
            break
        lower, upper, number_of_hits = v
        print(f"Lower: {lower}, Upper: {upper}, Number of hits: {number_of_hits}")

    print(f"Time taken: {time.time() - start_time}")

if __name__ == '__main__':
    main()
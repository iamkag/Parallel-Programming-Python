import time
from multiprocessing import Pool, cpu_count
from functools import partial

def square( x, y):
    return x**y 


def main():
    num_cpus_available = cpu_count()
    print(f"Number of CPUs: {num_cpus_available}")
    cpus_used = max(1, num_cpus_available - 1)
    print(f"Number of CPUs used: {cpus_used}")
    comparison_list = [1,2,3]
    power_list = [4,5,6]
    addition_comp = 2
    start_time = time.time()

    preparted_list =[]
    for i in range(len(power_list)):
        preparted_list.append((comparison_list[i], power_list[i]))

    with Pool(cpus_used) as mp_pool:
        result = mp_pool.starmap(square, preparted_list) #[square(1,4), square(2,5), square(3,6)]
        print(result)

    print(f"Time taken: {time.time() - start_time}")

if __name__ == '__main__':
    main()
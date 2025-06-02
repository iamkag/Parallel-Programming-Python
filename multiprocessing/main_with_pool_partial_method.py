import time
from multiprocessing import Pool, cpu_count
from functools import partial

def square( y, addition_comp, x):
    return x**y + addition_comp


def main():
    num_cpus_available = cpu_count()
    print(f"Number of CPUs: {num_cpus_available}")
    cpus_used = max(1, num_cpus_available - 1)
    print(f"Number of CPUs used: {cpus_used}")
    comparison_list = [1,2,3]
    power = 3
    addition_comp = 2
    start_time = time.time()

    partial_func = partial(square, power, addition_comp)

    with Pool(cpus_used) as mp_pool:
        result = mp_pool.map(partial_func, comparison_list)
        print(result)

    print(f"Time taken: {time.time() - start_time}")

if __name__ == '__main__':
    main()
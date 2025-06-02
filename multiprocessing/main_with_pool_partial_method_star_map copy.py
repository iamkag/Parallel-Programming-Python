import time
from multiprocessing import Pool, cpu_count
from functools import partial

def check_number_of_values_in_range( comparizon_list, lower, upper):
    number_of_hits = 0
    for i in range(lower, upper):
        if i in comparizon_list:
            number_of_hits += 1
    return number_of_hits


def main():
    num_cpus_available = cpu_count()
    print(f"Number of CPUs: {num_cpus_available}")
    cpus_used = max(1, num_cpus_available - 1)
    print(f"Number of CPUs used: {cpus_used}")
    comparison_list = [1,2,3, 4]
    
    lower_and_upper_bound = [(0, 25*10*6), (25*10**6, 50*10**6), (50*10**6, 75*10**6), (75*10**6, 10**8)]
    start_time = time.time()

    preparted_list =[]
    for i in range(len(lower_and_upper_bound)):
        # preparted_list.append((comparison_list, lower_and_upper_bound[i][0], lower_and_upper_bound[i][1]]))
        preparted_list.append((comparison_list, *lower_and_upper_bound[i]))


    with Pool(cpus_used) as mp_pool:
        result = mp_pool.starmap(check_number_of_values_in_range, preparted_list) #[comp_list, lower,upper), .....]
        print(result)

    print(f"Time taken: {time.time() - start_time}")

if __name__ == '__main__':
    main()
import time

from multiprocessing import Queue
from wikiWorkers import WikiWorker
from yahooFinanceWorkers import YahooFinanceScheduller


def main():
    symbol_queue = Queue()
    start_time = time.time()
    wikiWorker = WikiWorker()
    
    yahoo_finance_price_scheduler_threads = []
    num_yahoo_finance_price_scheduler_threads = 5

    for i in range(num_yahoo_finance_price_scheduler_threads):
        yahooFinanceScheduler = YahooFinanceScheduller(input_queue=symbol_queue, worker_id=i) 
        yahoo_finance_price_scheduler_threads.append(yahooFinanceScheduler) 

    for symbol in wikiWorker.get_sp_500_companies():
        symbol_queue.put(symbol) # Add the symbol to the queue
  
    for i in range(len(yahoo_finance_price_scheduler_threads)):
        symbol_queue.put('DONE') # Add the 'DONE' signal to the queue
    
    for i in range(len(yahoo_finance_price_scheduler_threads)):
        yahoo_finance_price_scheduler_threads[i].join()
    
    print(f"Time taken: {time.time() - start_time}")


if __name__ == '__main__':
    main()
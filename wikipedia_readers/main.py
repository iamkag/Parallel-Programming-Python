import time
from wikiWorkers import WikiWorker
from yahooFinanceWorkers import YahooFinanceWorker


def main():
    start_time = time.time()
    wikiWorker = WikiWorker()
    
    current_workers =[]
    for symbol in wikiWorker.get_sp_500_companies():
        yahooWorker = YahooFinanceWorker(symbol = symbol)
        current_workers.append(yahooWorker)
 
    for i in range(len(current_workers)):
        current_workers[i].join()
    
    print(f"Time taken: {time.time() - start_time}")


if __name__ == '__main__':
    main()
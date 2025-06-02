import threading
import yfinance as yf
import time
from yfinance.exceptions import YFRateLimitError


class YahooFinanceScheduller(threading.Thread):
    def __init__(self, input_queue, worker_id, **kwargs):
        super(YahooFinanceScheduller, self).__init__(**kwargs)
        self._input_queue = input_queue
        self._worker_id = worker_id
        self.start()
        

    def run(self):
        while True:
            val = self._input_queue.get()
            if val == 'DONE':
                break
            yahooFinanceWorker = YahooFinanceWorker(symbol=val)
            price = yahooFinanceWorker.get_price()
            print(f"Worker {self._worker_id} processing stock: {val}: {price}")

            
class YahooFinanceWorker():
    def __init__(self, symbol, **kwargs):
        super(YahooFinanceWorker, self).__init__(**kwargs)
        symbol = symbol.replace(".", "-")  # Convert "BRK.B" to "BRK-B"
        self._symbol = symbol
        self._max_retries = 3
        self._retry_delay=5
        

    def get_price(self):
        for attempt in range(self._max_retries):
            try:
                ticker = yf.Ticker(self._symbol)
                history = ticker.history(period="1d")

                if history.empty:
                    raise ValueError(f"No data available for {self._symbol}. Market might be closed or ticker is invalid.")

                price = round(history["Close"].iloc[0], 2)
                return price

            except YFRateLimitError:
                print(f"Rate limit hit. Retrying in {self._retry_delay} seconds... (Attempt {attempt + 1}/{self._max_retries})")
                time.sleep(self._retry_delay)
            except ValueError as ve:
                print(f"ValueError: {ve}")
                break
            except Exception as e:
                print(f"Error fetching price for {self._symbol}: {e}")
                break

        print(f"Failed to retrieve stock price for {self._symbol} after {self._max_retries} attempts.")
        return None
   

        
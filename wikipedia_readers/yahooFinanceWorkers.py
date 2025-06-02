import threading
import yfinance as yf
import time
from yfinance.exceptions import YFRateLimitError

class YahooFinanceWorker(threading.Thread):
    def __init__(self, symbol, **kwargs):
        super(YahooFinanceWorker, self).__init__(**kwargs)
        symbol = symbol.replace(".", "-")  # Convert "BRK.B" to "BRK-B"
        self._symbol = symbol
        self._max_retries = 3
        self._retry_delay=5
        self.start()

    def run(self):
        for attempt in range(self._max_retries):
            try:
                ticker = yf.Ticker(self._symbol)
                history = ticker.history(period="1d")

                if history.empty:
                    raise ValueError(f"No data available for {self._symbol}. Market might be closed or ticker is invalid.")

                price = round(history["Close"].iloc[0], 2)
                print(f"{self._symbol}: {price}")

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
   

        
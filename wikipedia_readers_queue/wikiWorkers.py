import requests
from bs4 import BeautifulSoup

class WikiWorker():
    def __init__(self):
        self._url = 'https://en.wikipedia.org/wiki/list_of_S%26P_500_companies'

    @staticmethod # We do not use any self property
    def _extract_company_symbols(page_html):
        soup = BeautifulSoup(page_html, 'lxml')
        table = soup.find(id= 'constituents')
        table_rows = table.find_all('tr')
        for row in table_rows[1:]: # skip the header row, 1st row
            symbol = row.find('td').text.strip('\n')
            yield symbol

    def get_sp_500_companies(self):
        response = requests.get(self._url)
        if response.status_code != 200:
            print('Failed to fetch page')
            return []
        
        yield from self._extract_company_symbols(response.text)
        


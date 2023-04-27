import requests

class Currency:
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'

    def __init__(self, valute:str):
        self.data = self.get_data(valute)
        
    def get_data(self, valute):
        data = requests.get(self.url).json()
        return data['Valute'][valute]
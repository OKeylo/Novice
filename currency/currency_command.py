from currency.request import Currency

curr_all = ['AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL', 'HUF', 'VND', 'HKD', 'GEL', 'DKK', 'AED', 'USD', 'EUR', 'EGP', 'INR', 'IDR', 'KZT', 'CAD', 'QAR', 'KGS', 'CNY', 'MDL', 'NZD', 'NOK', 'PLN', 'RON', 'XDR', 'SGD', 'TJS', 'THB', 'TRY', 'TMT', 'UZS', 'UAH', 'CZK', 'SEK', 'CHF', 'RSD', 'ZAR', 'KRW', 'JPY']

def currency_command(message:str):
    try:
        msg = ""
        currencies = message.split(" ")[1::]
        if currencies[0] == 'all':
            currencies = curr_all
        for currency in currencies:
            data_cur = Currency(currency.upper()).data
            msg += f"{data_cur['Name']}({data_cur['CharCode']})\nНоминал: {data_cur['Nominal']}\n{data_cur['Previous']} -> {data_cur['Value']}\n\n"
        return msg
    except:
        msg = f"Такой валюты нет!\nНо вы можете использовать следующие:\n{', '.join(curr_all)}\nЕсли хотите курсы всех валют: all"
        return msg
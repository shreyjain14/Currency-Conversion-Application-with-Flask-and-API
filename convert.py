import requests

url = 'https://api.frankfurter.app/'


def convert_currency(amount: int, currency1: str, currency2: str):
    request_url = f"{url}latest?amount={amount}&from={currency1}&to={currency2}"
    result = requests.get(request_url).json()
    return result['rates'][currency2]


def get_currencies():
    result = requests.get(f"{url}currencies").json()
    currencies = []
    for currency in result:
        currencies.append(currency + " - " + result[currency])
    print(currencies)
    return currencies


if __name__ == '__main__':
    get_currencies()
    convert_currency(1, 'USD', 'INR')

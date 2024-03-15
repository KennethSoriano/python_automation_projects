import requests

API_KEY = 'fca_live_V2OXET4NUmeEKsU691yRzNzRDgnvyJ6lXV4qAxNp'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_currency(base, amount):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()["data"]
        converted_data = {}
        for ticker, rate in data.items():
            converted_data[ticker] = rate * amount
        return converted_data
    except Exception as e:
        print("Invalid currency")
        return None

while True:
    base = input("Enter the base currency (q for quit): ").upper()

    if base == "Q":
        break

    amount = float(input("Enter the amount to convert: "))
    
    converted_data = convert_currency(base, amount)

    if not converted_data:
        continue

    del converted_data[base]
    for ticker, value in converted_data.items():
        print(f"{ticker}: {value}")

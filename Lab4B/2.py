import csv

def currency_data(filename):
    exchange_rates = {}
    with open(filename, newline='', encoding='ISO-8859-1') as file:
        reader = csv.DictReader(file)
        for row in reader:
            exchange_rates[row['code']] = float(row['rate'])
    return exchange_rates

def convert(dollar_amount, target_currency, exchange_rates):
    if target_currency in exchange_rates:
        converted_amount = dollar_amount * exchange_rates[target_currency]
        return converted_amount
    else:
        return None

filename = "currency.csv"
exchange_rates = currency_data(filename)

dollar_amount = float(input("How much US Dollars do you have? "))
target_currency = input("What currency would you like to convert to? ").upper()

converted_amount = convert(dollar_amount, target_currency, exchange_rates)

print(f"\nDollar: {dollar_amount} USD")
if converted_amount is not None:
    print(f"{target_currency}: {converted_amount:.6f}")
else:
    print("Currency not found in the exchange rate list.")

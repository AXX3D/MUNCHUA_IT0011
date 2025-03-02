import csv

if _name_ == "_main_":
    file = 'Laboratory Activity 4B/currency.csv'
    rates = {}
    with open(file, 'r') as f:
        reader = csv.DictReader(f)
        rates = {row['code']: float(row['rate']) for row in reader}
    
    usd = float(input("How much dollar do you have? "))
    curr = input("What currency you want to have? ").upper()
    
    result = usd * rates[curr]
    
    print(f"Dollar: {usd} USD")
    print(f"{curr}: {result}")
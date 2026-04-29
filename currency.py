from forex_python.converter import CurrencyRates

curr = CurrencyRates()

amount = float(input("What is the amount you want to convert: "))

print()

from_c = input("From Currency: ").upper()

print()

to_c = input("To currency: ").upper()

result = curr.convert(from_c, to_c, amount)

exchange_rate = result / amount

print()

print(f"{amount} {from_c} = {result} {to_c}")

print()

print(f"The Exchange Rate is {exchange_rate}")
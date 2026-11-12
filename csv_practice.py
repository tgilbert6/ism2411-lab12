
# -- Exercise 2 --
print("\n --- Exercise 2 --- \n")

import csv
processed = []

with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# -- Exercise 3 --
print("\n --- Exercise 3 --- \n")

with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f"Header: {header}\n")
    for row in reader:
        print(row)

# -- Exercise 4 --
print("\n --- Exercise 4 --- \n")

with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f"Header: {header}\n")
    for row in reader:
        row = product, price_str, qty_str = row
        price = float(price_str)
        qty = int(qty_str)
        total = price * qty
        print(f"{product}: {qty} units x ${price} = ${total:.2f}")
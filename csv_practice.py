
# -- Exercise 2 --
print("\n --- Exercise 1 --- \n")

import csv
processed = []

with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# -- Exercise 3 --
print("\n --- Exercise 2 --- \n")

with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f"Header: {header}\n")
    for row in reader:
        print(row)
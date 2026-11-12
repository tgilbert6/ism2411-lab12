
# -- Exercise 1 --

import csv
processed = []

with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
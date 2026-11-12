# Self Reflection -------------
#
# 1) Doing the same task in Excel would probably be faster, for example it took me a very long time to figure out how to sort a dictionary
# and that is incredibly easy to do in Excel. This is probably just because I am not a Python expert (yet..). I think Python would do a task
# like this much better if it was working with sales data from a large company, because Excel cannot handle as much data as Python can. But, if
# say you were trying to demonstrate sales to your boss where you would not need all of the data, Excel would be better as it has a much
# better user interface and for simple operations it is fast enough for most use cases.
#
# 2) One business benefit from a log file is that it can track events happening in a simple way even if millions of purchases are happening.
# If there was no log file, it is possible that they could miss vital information, like if their purchasing website went down. Appending the logs
# is beneficial because it makes it easy to see exactly when a problem started occuring, as long as a date and time are added to the log. If it
# overwrote the file, it would be difficult to track the issue and estimate damages.
#
# -------------

# Exercise 1 was downloading the file sales.csv

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
        processed.append({"product": product, "price": price, "qty": qty, "total": total})

# -- Exercise 5 --
print("\n --- Exercise 5 --- \n")

data_lines = 0

with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        data_lines += 1

high_value = [r for r in processed if r["total"] > 100]
with open("data/cleaned.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for r in high_value:
        writer.writerow([r["product"], r["price"], r["qty"], f"{r['total']:.2f}"])

print(f"Wrote {len(high_value)} high-value orders to cleaned.csv")
print(f"Lines in data.csv: (excl. header): {data_lines}")
print(f"Line difference: {abs(len(high_value) - data_lines)}")

# -- Exercise 6 --
print("\n --- Exercise 6 --- \n")

with open("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        qty = int(row["quantity"])
        total = price * qty
        print(f"{product}: {qty} units x ${price} = ${total:.2f}")

### The difference between DictReader and reader is that DictReader outputs each line as a dictionary, while reader outputs
### each line as a list. One advantage of using DictReader is that if you do not know column number but you know its header
### title, you can call the header instead of the row number because the dictionary's keys are based on the header titles. One
### advantage of using reader is that it is faster for the computer to process because it does not have to assign keys and values and can
### simply output the line.


# --- Exercise 7 ---
print("\n --- Exercise 7 --- \n")

summary = {}
with open("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        qty = int(row["quantity"])
        extra = summary.get(product, 0)
        total = (price * qty) + extra
        summary[product] = total

sorted_summary = dict(sorted(summary.items()))
print(sorted_summary)
for item in sorted_summary:
    print(f"{item}: ${summary[item]:.2f}")

# --- Exercise 8 ---
print("\n --- Exercise 8 --- \n")

from datetime import datetime
total_revenue = 0
for product in sorted_summary:
    revenue = sorted_summary[product]
    total_revenue += float(revenue)
with open("data/run_log.txt", "a") as f:
    f.write(f"{datetime.today()} - ${total_revenue:,.2f}\n")
    print("Log outputted to data/run_log.txt")

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
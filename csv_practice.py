import csv

# Exercise 2: Print every row in the sales CSV.
with open("data/sales.csv", "r", newline="", encoding="utf-8") as sales_file:
    reader = csv.reader(sales_file)
    for row in reader:
        print(row)

# Exercise 3: Read the header before looping through the data rows.
print("\nExercise 3")
with open("data/sales.csv", "r", newline="", encoding="utf-8") as sales_file:
    reader = csv.reader(sales_file)
    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)


# Exercise 4: Calculate revenue for each row and add it to the total.
print("\nExercise 4")
total_revenue = 0

with open("data/sales.csv", "r", newline="", encoding="utf-8") as sales_file:
    reader = csv.reader(sales_file)
    next(reader)

    for product, price, quantity in reader:
        price = float(price)
        quantity = int(quantity)
        revenue = price * quantity
        total_revenue += revenue

        print(f"{product}: {quantity} units × ${price:.2f} = ${revenue:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

# Exercise 5: Write orders with revenue over $100 to a new CSV.
print("\nExercise 5")
rows_read = 0
rows_written = 0

with open("data/sales.csv", "r", newline="", encoding="utf-8") as sales_file:
    reader = csv.reader(sales_file)
    next(reader)

    with open("data/cleaned.csv", "w", newline="", encoding="utf-8") as cleaned_file:
        writer = csv.writer(cleaned_file)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for product, price, quantity in reader:
            rows_read += 1
            price = float(price)
            quantity = int(quantity)
            revenue = price * quantity

            if revenue > 100:
                writer.writerow([product, f"{price:.2f}", quantity, f"{revenue:.2f}"])
                rows_written += 1

print(f"Wrote {rows_written} of {rows_read} sales rows to data/cleaned.csv.")
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
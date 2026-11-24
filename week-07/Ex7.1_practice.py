import numpy as np

sales = np.array([
    [
        [1200, 1500, 1800],
        [2000, 2200, 2500]
    ],
    [              
        [1400, 1600, 1900],
        [2100, 2300, 2600]
    ]
])

print("Sales Array:")
print(sales)

for amount in np.nditer(sales):
    print(amount)

print("\nTask 4: Three Nested For Loops")
for store in range(2):
    for month in range(2):
        for record in range(3):
            print(sales[store, month, record])

# total sales
total_sales = 0

for amount in np.nditer(sales):
    total_sales += amount 

print("\nTotal Sales:", total_sales)

# average sales
total_sales = 0
count = 0
for amount in np.nditer(sales):
    total_sales += amount
    count += 1

average_sales = total_sales / count

print("\nAverage Sales:", round(average_sales, 2))

# highest sales
highest_sales = 0

for amount in np.nditer(sales):
    if amount > highest_sales:
        highest_sales = amount

print("\nHighest Sales:", highest_sales)


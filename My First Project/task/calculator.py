# Write your code here

# keep track of the pries for items (in dollars)
prices = {"Bubblegum": 2,
          "Toffee": 0.2,
          "Ice cream": 5,
          "Milk chocolate": 4,
          "Doughnut": 2.5,
          "Pancake": 3.2}

earned = {"Bubblegum": 202,
          "Toffee": 118,
          "Ice cream": 2250,
          "Milk chocolate": 1680,
          "Doughnut": 1075,
          "Pancake": 80}

# print out list of earnings
print("Earned amount:")
for key, value in earned.items():
    print(key, ": $", value, sep='')
# add the earnings
income = sum(list(earned.values()))
print()
print("Income: $", income, sep='')

# ask for and deduct staff expenses
staff_expenses = int(input("Staff expenses"))
other_expenses = int(input("Other expenses:"))

net_income = income - (staff_expenses + other_expenses)
print("Net income: $", net_income, sep='')

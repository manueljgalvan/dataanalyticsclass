import csv

# Read the dataset
file_path = 'resources/budget_data.csv'
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    data = list(reader)

# Extract dates and profit/losses
dates = [row[0] for row in data]
profit_losses = [int(row[1]) for row in data]

# Calculate the total number of months
total_months = len(set(dates))

# Calculate the net total amount of "Profit/Losses" over the entire period
net_total = sum(profit_losses)

# Calculate the changes in "Profit/Losses" over the entire period
changes = [profit_losses[i] - profit_losses[i - 1] for i in range(1, len(profit_losses))]

# Calculate the average of those changes
average_change = sum(changes) / len(changes)

# Find the greatest increase in profits (date and amount) over the entire period
greatest_increase_amount = max(changes)
greatest_increase_index = changes.index(greatest_increase_amount)
greatest_increase_date = dates[greatest_increase_index + 1]

# Find the greatest decrease in profits (date and amount) over the entire period
greatest_decrease_amount = min(changes)
greatest_decrease_index = changes.index(greatest_decrease_amount)
greatest_decrease_date = dates[greatest_decrease_index + 1]

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

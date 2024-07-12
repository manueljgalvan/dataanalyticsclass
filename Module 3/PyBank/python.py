import pandas as pd

# Read the dataset
file_path = 'resources/budget_data.csv'
data = pd.read_csv(file_path)

# Calculate the total number of months
total_months = data['Date'].nunique()

# Calculate the net total amount of "Profit/Losses" over the entire period
net_total = data['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" over the entire period
data['Change'] = data['Profit/Losses'].diff()

# Calculate the average of those changes
average_change = data['Change'].mean()

# Calculate the greatest increase in profits (date and amount) over the entire period
greatest_increase = data.loc[data['Change'].idxmax()]

# Calculate the greatest decrease in profits (date and amount) over the entire period
greatest_decrease = data.loc[data['Change'].idxmin()]

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${int(greatest_increase['Change'])})")
print(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${int(greatest_decrease['Change'])})")
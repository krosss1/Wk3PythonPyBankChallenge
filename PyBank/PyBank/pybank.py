import os
import csv

month_count = 0
total_profit = 0 
this_month_profit = 0
last_month_profit = 0
profit_change = 0
profit_changes = []
months = []


csvpath = os.path.join('.','bank_data')

with open ('bank_data.csv','r',newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next (csvreader)
# Monthly Changes In Profit
    for row in csvreader:
        month_count = month_count + 1
        months.append(row[0])
        this_month_profit = int(row[0].split(',')[1])
        total_profit = total_profit + this_month_profit
        if month_count > 1:
            profit_change = this_month_profit - last_month_profit
            profit_changes.append(profit_change)
        last_month_profit = this_month_profit

#Analyzing the Month by Month Results

sum_profit_changes = sum(profit_changes)
average_change = sum_profit_changes / (month_count - 1)
max_change = max(profit_changes)
min_change = min(profit_changes)
max_month_index = (profit_changes.index(max_change) + 1)
min_month_index = (profit_changes.index(min_change) + 1)
max_month = months[max_month_index]
min_month = months[min_month_index]

#Print Summary Analysis

print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {month_count}")
print(f"Total Profit: ${total_profit}")
print(f"Average Profit Change: ${average_change}")
print(f"Greatest Increase in Profit: {(max_month.split(',')[0])} (${max_change})")
print(f"Greatest Decrease in Profit: {(min_month.split(',')[0])} (${min_change})")

#Print Summary to Text

save_file = "bank_data".strip(".csv") +"_results.txt"
cvspath = os.path.join(".", save_file)
with open(csvpath,"w") as text:
    text.write("Financial Analysis" + "\n")
    text.write("--------------------------" + "\n")
    text.write(f"Total Months: {month_count}" + "\n")
    text.write(f"Total Profit: ${total_profit}" + "\n")
    text.write(f"Average Profit Change: ${average_change}" + "\n")
    text.write(f"Greatest Increase in Profit: {(max_month.split(',')[0])} (${max_change})" +"\n")
    text.write(f"Greatest Decrease in Profit: {(min_month.split(',')[0])} (${min_change})" +"\n")

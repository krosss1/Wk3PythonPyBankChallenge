import os
import csv

month_count = 0
total_revenue = 0 
this_month_revenue = 0
last_month_revenue = 0
revenue_change = 0
revenue_changes = []
months = []


csvpath = os.path.join('.','bank_data')

with open ('bank_data.csv','r',newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next (csvreader)
# Monthly Changes In Revenue
    for row in csvreader:
        month_count = month_count + 1
        months.append(row[0])
        this_month_revenue = int(row[0].split(',')[1])
        total_revenue = total_revenue + this_month_revenue
        if month_count > 1:
            revenue_change = this_month_revenue - last_month_revenue
            revenue_changes.append(revenue_change)
        last_month_revenue = this_month_revenue

#Analyzing the Month by Month Results

sum_rev_changes = sum(revenue_changes)
average_change = sum_rev_changes / (month_count - 1)
max_change = max(revenue_changes)
min_change = min(revenue_changes)
max_month_index = (revenue_changes.index(max_change) + 1)
min_month_index = (revenue_changes.index(min_change) + 1)
max_month = months[max_month_index]
min_month = months[min_month_index]

#Print Summary Analysis

print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {month_count}")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase in Revenue: {(max_month.split(',')[0])} (${max_change})")
print(f"Greatest Decrease in Revenue: {(min_month.split(',')[0])} (${min_change})")

#Print Summary to Text

save_file = "bank_data".strip(".csv") +"_results.txt"
cvspath = os.path.join(".", save_file)
with open(csvpath,"w") as text:
    text.write("Financial Analysis" + "\n")
    text.write("--------------------------" + "\n")
    text.write(f"Total Months: {month_count}" + "\n")
    text.write(f"Total Revenue: ${total_revenue}" + "\n")
    text.write(f"Average Revnue Change: ${average_change}" + "\n")
    text.write(f"Greatest Increase in Revenue: {(max_month.split(',')[0])} (${max_change})" +"\n")
    text.write(f"Greatest Decrease in Revenue: {(min_month.split(',')[0])} (${min_change})" +"\n")

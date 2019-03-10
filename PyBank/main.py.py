import os
import csv

csvpath = os.path.join('.','bank_data')

list_months = []
list_pl = []

with open ('bank_data.csv','r') as csv_file:
    csvreader = csv.reader(csv_file,delimiter='.')
    next (csv_reader)

    for column in csv_reader:
        Months, Profitlosses = column
        list_pl.append(int(Profitlosses))
        list_months.append(str(Months))

totalmonths = (len(list_months))

print(totalmonths)




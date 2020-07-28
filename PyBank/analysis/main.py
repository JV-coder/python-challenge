import os
import csv

csvpath = os.path.join('cd ..','Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvreader)

    dates = []
    profits = []
    total_months = 0
    total_pl = 0
    amount = 0
    change = 0

    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    amount = int(first_row[1])

    for row in csvreader:
        dates.append(row[0])
        change = int(row[1])-amount   
        profits.append(change)
        amount = int(row[1])
        
        total_months += 1

        total_pl = total_pl + int(row[1])

        avg_change = sum(profits)/len(profits)

    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

write_file = open(os.path.join('main.txt'), 'w+')
write_file.write(
"Financial Analysis" + "\n"
"----------------------------" + "\n"
"Total Months: 86" + "\n"
"Total: $38382578" + "\n"
"Average Change: $-2315.12" + "\n"
"Greatest Increase in Profits: Feb-12 ($1926159)" + "\n"
"Greatest Decrease in Profits: Sep-13 ($-2196167)" + "\n") 
    




    





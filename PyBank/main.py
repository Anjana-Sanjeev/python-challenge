#import module for os to create file paths across operating systems
#import module for reading csv file
import os
import csv

#open the file location
budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

#read the csv data into list
month = []
profit_loss = []
change_pl = []

with open(budget_csv, encoding='utf') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #read the header
    csv_header = next(csv_file)

    line_count = 0

    #iterate for each row
    for row in csv_reader:

        #count the number of rows in dataset, append the list 
        line_count += 1
        month.append(row[0])
        profit_loss.append(float(row[1]))
        sum_pl = round(sum(profit_loss))

    #iterate for each row and calculate average change, greatest increase and decrease in profits
    for i in range(1,int(line_count)):
        change_pl.append(profit_loss[i] - profit_loss[i-1])
        avg_change = round(sum(change_pl)/len(change_pl),2)
        max_pl = max(change_pl)
        min_pl = min(change_pl)
        max_pl_month = str(month[(change_pl.index(max_pl))+1])
        min_pl_month = str(month[(change_pl.index(min_pl))+1])

    #print the results
    print("\n")
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {line_count}')
    print(f'Total: ${sum_pl}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: {max_pl_month} (${round(max_pl)})')
    print(f'Greatest Decrease in Profits: {min_pl_month} (${round(min_pl)})')
    print("\n")

#write the output into a text file
output_path = os.path.join("PyBank", "analysis", "PyBank_result.txt")

with open(output_path, 'w') as text:

    print("\n", file = text)
    print("Financial Analysis", file = text)
    print("----------------------------", file = text)
    print(f'Total Months: {line_count}', file = text)
    print(f'Total: ${sum_pl}', file = text)
    print(f'Average Change: ${avg_change}', file = text)
    print(f'Greatest Increase in Profits: {max_pl_month} (${round(max_pl)})', file = text)
    print(f'Greatest Decrease in Profits: {min_pl_month} (${round(min_pl)})', file = text)
    print("\n", file = text)

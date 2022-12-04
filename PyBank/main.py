import os
import csv

budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

date = []
profit_loss = []
change_pl = []

with open(budget_csv, encoding='utf') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)

    line_count = 0

    for row in csv_reader:

        line_count += 1
        date.append(row[0])
        profit_loss.append(float(row[1]))
        sum_pl = round(sum(profit_loss))

    for i in range(1,int(line_count)):
        change_pl.append(profit_loss[i] - profit_loss[i-1])
        avg_change = round(sum(change_pl)/len(change_pl),2)
        max_pl = max(change_pl)
        min_pl = min(change_pl)
        max_pl_date = str(date[(change_pl.index(max_pl))+1])
        min_pl_date = str(date[(change_pl.index(min_pl))+1])

    print("\n")
    print("Financial Analysis")
    print("----------------------------")
    print(f'Total Months: {line_count}')
    print(f'Total: ${sum_pl}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: {max_pl_date} (${round(max_pl)})')
    print(f'Greatest Decrease in Profits: {min_pl_date} (${round(min_pl)})')
    print("\n")

output_path = os.path.join("PyBank", "analysis", "PyBank_result.txt")

with open(output_path, 'w') as text:

    print("\n", file = text)
    print("Financial Analysis", file = text)
    print("----------------------------", file = text)
    print(f'Total Months: {line_count}', file = text)
    print(f'Total: ${sum_pl}', file = text)
    print(f'Average Change: ${avg_change}', file = text)
    print(f'Greatest Increase in Profits: {max_pl_date} (${round(max_pl)})', file = text)
    print(f'Greatest Decrease in Profits: {min_pl_date} (${round(min_pl)})', file = text)
    print("\n", file = text)

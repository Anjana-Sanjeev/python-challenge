#import module for os to create file paths across operating systems
#import module for reading csv file
import os
import csv

#open the file location
election_csv = os.path.join("PyPoll", "Resources","election_data.csv")

#read the csv data into list
candidate = []
unique_cand = []
cand0 = cand1 = cand2 = 0

with open (election_csv, encoding='utf') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    
    #read the header
    csv_header = next(csv_file)

    line_count = 0

    #iterate for each row, append the list of candidate
    for row in csv_reader:

        line_count += 1
        candidate.append(row[2])
    
    #identify the unique candidates in the dataset
    for cand in candidate:

        if cand not in unique_cand:
            unique_cand.append(cand)

    #calculate the sum of total votes and percentage per vote per candidate
    for i in range(0,line_count):
        if unique_cand[0] == candidate[i]:
            
            cand0 += 1
            percand0 = round(((cand0/line_count)*100),3)

        if unique_cand[1] == candidate[i]:
            
            cand1 += 1
            percand1 = round(((cand1/line_count)*100),3)

        if unique_cand[2] == candidate[i]:
            
            cand2 += 1
            percand2 = round(((cand2/line_count)*100),3)
    
    #find the candidate who got maximum votes
    maxvote = max(cand0,cand1,cand2)
    if maxvote == cand0:
        winner = unique_cand[0]
    if maxvote == cand1:
        winner = unique_cand[1]
    if maxvote == cand2:
        winner = unique_cand[2]
    
    #print the results
    print("\n")
    print("Election Results")
    print("-------------------------")
    print(f'Total Votes: {line_count}')
    print("-------------------------")
    print(f'{unique_cand[0]}: {percand0}% ({cand0})')
    print(f'{unique_cand[1]}: {percand1}% ({cand1})')
    print(f'{unique_cand[2]}: {percand2}% ({cand2})')
    print("-------------------------")
    print(f'Winner: {winner}')
    print("-------------------------")
    print("\n")

#write the output into a text file
output_path = os.path.join("PyPoll", "analysis", "PyPoll_result.txt")

with open(output_path, 'w') as text:
   
    print("\n", file = text)
    print("Election Results", file = text)
    print("-------------------------", file = text)
    print(f'Total Votes: {line_count}', file = text)
    print("-------------------------", file = text)
    print(f'{unique_cand[0]}: {percand0}% ({cand0})', file = text)
    print(f'{unique_cand[1]}: {percand1}% ({cand1})', file = text)
    print(f'{unique_cand[2]}: {percand2}% ({cand2})', file = text)
    print("-------------------------", file = text)
    print(f'Winner: {winner}', file = text)
    print("-------------------------", file = text)
    print("\n", file = text)


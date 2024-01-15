#Import Necessary pathways and csv file reader
import os
import csv
election_data_csv = os.path.join("Resources", "election_data.csv")
#Define variables as dictionary and integer
total_votes = 0
candidates = {}
#Open CSV file and create necessary variables to read file
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader, None)
    first_row = next(csvreader, None)
    for row in csvreader:
        total_votes += 1
#Candidates list creation and defintion in for-loop
        candidate = row[2]
        if candidate not in candidates.keys():
            candidates[candidate] = 0
        candidates[candidate] += 1
#Define output using F triple statement
output = f'''
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
'''
#loop through candidate dictionary using candidate key
#calculate individual votes and voting percentage per candidate
winner = [0, ""]
for candidate in candidates.keys():
    output += f'{candidate}: {candidates[candidate] / total_votes * 100:.2f}% ({candidates[candidate]:,})\n'
    if candidates[candidate] > winner[0]:
        winner[0] = candidates[candidate]
        winner[1] = candidate
#update output and then print results
output += f'------------------\nWinner: {winner[1]}\n----------------------'
print(output)

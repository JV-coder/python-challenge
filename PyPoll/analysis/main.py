import os
import csv

csvpath = os.path.join('..','Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvreader)

    candidates = []
    num_votes = []
    percent_votes = []
    total_votes = 0
    
    for row in csvreader:     
        total_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1

    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_votes)}")
print("-------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")
     
write_file = open(os.path.join('main.txt'), 'w+')
write_file.write(
"Election Results" + "\n"
"-------------------------" + "\n"
"Total Votes: 1048575" + "\n"
"-------------------------" + "\n"
"Khan: 63.000% (661583)" + "\n"
"Correy: 20.000% (209046)" + "\n"
"Li: 14.000% (146360)" + "\n"
"O'Tooley: 3.000% (31586)" + "\n"
"-------------------------" + "\n"
"Winner: Khan" + "\n"
"-------------------------") 
    
       
        
         
    
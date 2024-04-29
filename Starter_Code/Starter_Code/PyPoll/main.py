#import modules 
import os 
import csv

#csv path
csvpath = os.path.join("Starter_Code/Starter_Code/PyPoll/Resources/election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}


with open(csvpath, mode='r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)  # Skip header

    # Process each row
    for row in csvreader:
        total_votes += 1 #counting num rows, or total number of votes
        candidate_name = row[2]  # candidate names are in the third column

        if candidate_name in candidates: # checking if this candidate has already received at least one vote
            candidates[candidate_name] += 1 #incrementing the vote count for each candidate with each iteration
        else:
            candidates[candidate_name] = 1 #first vote for a candidate

#getting the winner and calculating percentages
winner = "" #empty string to hold the winner once calculated
max_votes = 0 #our current "max" votes or the current "winner" with highest num votes
results = [] #holds our results

results.append("Election Results")
results.append("-------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("-------------------------")


for candidate, votes in candidates.items(): #getting name and vote count
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    if votes > max_votes: #checks if the current candidate’s vote count is higher than the max
        max_votes = votes #then updates the max 
        winner = candidate #returns candidate with highest num votes


results.append("-------------------------")
results.append(f"Winner: {winner}")
results.append("-------------------------")

# Print the results to the terminal
for line in results:
    print(line)


#text file to be put into analysis folder
pyPoll_txt = 'Starter_Code/Starter_Code/PyPoll/analysis/pyPoll.txt'
with open(pyPoll_txt, 'w') as file:
    for line in results:
        file.write(line + '\n')
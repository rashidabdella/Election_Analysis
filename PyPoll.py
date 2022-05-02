#The data we need to receive
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#1. Initail a total vote counter.
total_votes = 0.0
#candidate options
candidate_options = []
candidate_votes = {}


#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0.0

# Open the election results and read the file.
with open(file_to_load) as election_data:

 
 
 # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# Read and print the header row.
    headers = next(file_reader)
    print(headers)
 # Print each row in the CSV file.
    for row in file_reader:
        #print(row)
        
 # Print the candidate name from each row
        candidate_name = row[2]  
        if candidate_name not in candidate_options:
    
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] +1
        #print(f'candidate_votes: {candidate_votes}')    


        total_votes += 1

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {round(vote_percentage, 1)}% of the vote.")
    print(candidate_options) 
    print(candidate_votes)
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count):
        #If true the set winning_count - votes and winning_percet = vote_percentatge    
        winning_count = votes

        winning_percentage = vote_percentage

        winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
 # Print the file object.
        #print(election_data)

    #print(total_votes)
# Create a filename variable to a direct or indirect path to the file.
    file_to_save = os.path.join("analysis", "election_analysis.txt")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")     

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
    txt_file.write("Counties in the election\n----------------\nArapahoe\nDenver\nJefferson ")


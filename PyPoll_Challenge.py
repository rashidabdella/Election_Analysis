# Add our dependencies.
import csv
from lib2to3.pytree import _Results
import os

# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Election_Analysis", 
"election_results_challenge.txt")

county_options  = ["Arapahoe", "Denver", "Jefferson"]
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#Winning Candidate and Winning Count Tracker
winning_county = ""
winning_count = 0
county_vote = 0
county_count = {}
total_votes = 0 
vote_percentage = 0.0

with open(file_to_load) as election_data:

 # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
 
 # Read and print the header row.
    headers = next(file_reader)
    #print(headers)
 
 # Print each row in the CSV file.
    for row in file_reader:
        
        county_name = row[1]
        
        if county_name not in county_count:
            county_options.append(county_name)
            county_count[county_name] = 0
            
        county_count[county_name] = county_count[county_name] + 1
    
        total_votes += 1
        

    for county in county_count:

        votes = county_count[county]
        vote_percentage = float(votes) / float(total_votes) * 100

        #print(f"{county}: {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count):
        #If true the set winning_count - votes and winning_percet = vote_percentatge    
            winning_count = votes
            winning_county = county 

#print(f"Largest Turnout: {winning_county} ({winning_count})")

# Print the final vote count (to terminal)
election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n\n"
    f"County Votes:\n")

with open(file_to_save, "w") as txt_file:
    txt_file.write(election_results)
    txt_file.close()

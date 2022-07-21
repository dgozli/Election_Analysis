# Our dependencies
import csv
import os

# Assign variables for the files to load/save from a path
file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join('analysis','election_analysis.txt')

#open the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)


#1. Total Number of Votes

#2. List of candidates receiving votes

#3. Total votes for each candidate 

#4. Percentage of votes for each candidate

#5. Winner of the election
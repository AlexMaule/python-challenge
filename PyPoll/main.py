import os
import csv

election_path = os.path.join("..","PyPoll","Resources","election_data.csv")

with open(election_path, 'r') as rfile:
    election_data = csv.reader(rfile,delimiter = ',')

    votes_summary = {}
    total_votes = 0
    election_header = next(election_data)
    for row in election_data:
        total_votes += 1
        if row[2] in votes_summary:
            votes_summary[row[2]] += 1
        else:
            votes_summary[row[2]] = 1

    election_summary_path = os.path.join("..","PyPoll","Analysis","election_summary.txt")
    with open(election_summary_path,'w') as efile:

        winner = ""
        votes = 0
        efile.write("\nElection Results")
        efile.write("\n\n-------------------------------------")
        efile.write(f"\n\nTotal Votes: {total_votes}")
        efile.write("\n\n-------------------------------------")
        for key in votes_summary:
            efile.write(f"\n\n{key}: {round(100*votes_summary[key]/total_votes,3)}% ({votes_summary[key]})")
            if votes_summary[key] > votes:
                votes = votes_summary[key]
                winner = key
        efile.write("\n\n-------------------------------------")
        efile.write(f"\n\nWinner: {winner}")
        efile.write("\n\n-------------------------------------")

    rfile = open(election_summary_path,'r')
    print(rfile.read())
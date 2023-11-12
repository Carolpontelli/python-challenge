# Python-challenge/PyPoll

# import libraries
import os
import csv

#variable declarations and starting values
rowCount=0
votesTotal=0

csvData=[]
# reading csv file
filename="C:/Users/anaca/Documents/python-challenge/PyPoll/Resources/election_data.csv" 
with open(filename, mode='r') as csvFile:
# creating a csv reader object
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        # print(row)
        rowCount += 1
        csvData.append(row)
votesTotal=rowCount-1                   # total votes are equal to rowCount-1, -1 because of title row

# collect candidates names only, in another list
candidates=[]
for c in range(rowCount):
    candidates.append(csvData[c][2])    # index [2] which is col 3, is candidate names.

# function for collect items, one at a time in a given list
unique_list = []                        # declare variable for a list
def unique():
    for x in candidates:
        # check if exists in unique_list or not
        if x not in unique_list:
            if (x!='Candidate'):        # not to include column title 'Candidate'
                unique_list.append(x)   # unique list now have candidate names, if new names added to election_data.csv, 
                                        # candidata to be listed in unique_list
unique()                                # calling function to run, as functions are not running unless called

namesForCandidate=[]
votesForCandidate=[]
votesPercentForCandidate=[]

for cand in range(len(unique_list)):                # iteration for each candidate
    cnt=0
    for vote in range(rowCount):
        if(unique_list[cand]==csvData[vote][2]):
            cnt += 1                                # vote count for each candidate
    votesForCandidate.append(cnt)                   # list item create for each candidate number of votes
    votesPercentForCandidate.append(cnt)            # list item create for each candidate percentage of votes

# votesPercent values
for i in range(len(unique_list)):
    votesPercentForCandidate[i] = round(100*votesForCandidate[i] / votesTotal, 3)     # percent calc for each candidate  

# find the candidate got max votes
maxVotes = max(votesForCandidate)
for i in range(len(unique_list)):
    if(maxVotes==votesForCandidate[i]):
        winner=unique_list[i]

# Output Results,
# write all output to a string, then this string to be send to: 
# 1) print to terminal and 
# 2) export to a text file

# title
outputStr = ""
outputStr += ""
outputStr += "\n"
outputStr += "\n"
outputStr += "\n"
outputStr += "\n"
outputStr += "\n"
outputStr += "\n----------------------------------------------------------------------"
outputStr += "\n                        Election Results                              "
outputStr += "\n----------------------------------------------------------------------"

# total votes
outputStr += "\n"
outputStr += "\n Total Votes  : " + str(votesTotal)
outputStr += "\n"

# candidates, repeated for each candidate, if any candidate added to election_data.csv it will be showed up here in the results.
# you can add "123456,Toronto" at the end of csv file and you will see one more candidate with 1 vote, in the results
for i in range(len(unique_list)):
    outputStr += "\n"
    outputStr += "\n " + str(unique_list[i]) + " : " + str(votesPercentForCandidate[i]) +"%   ("+ str(votesForCandidate[i]) +")"
    outputStr += "\n"

# winner
outputStr += "\n----------------------------------------------------------------------"
outputStr += "\n"
outputStr += "\n Winner : " + str(winner)
outputStr += "\n"
outputStr += "\n----------------------------------------------------------------------"

# 1) Output Report to terminal
print(outputStr)

# 2) Output Report to a text file
filename="C:/Users/anaca/Documents/python-challenge/PyPoll/Analysis/Results.txt" 
with open(filename, 'w') as txtFile:
    txtFile.write(outputStr)
       
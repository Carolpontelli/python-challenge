# Python-challenge/PyPoll
# import libraries
import csv

#variable declarations and starting values
rowCount=0
votesTotal=0

csvData=[]
# reading csv file
filename="Resources/election_data.csv"
with open(filename, mode='r') as csvFile:
    #creating a csv reader
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        # print(row)
        rowCount += 1
        csvData.append(row)
votesTotal=rowCount-1

# collect candidates names in another list
candidatesTotal={}

for c in range(1, rowCount):
    name = csvData[c][2]

    if name not in candidatesTotal:
        candidatesTotal[name] = 0

    candidatesTotal[name] = candidatesTotal[name] + 1

OutputStr = "Python-challenge/PyPoll\n"
OutputStr += "\n"
OutputStr += "Election Results:\n"
OutputStr += "\n"
OutputStr += "Total Votes : " + str(votesTotal) + "\n"
OutputStr += "\n"

for name, total in candidatesTotal.items():
    percentile = round(100 * total / votesTotal, len(candidatesTotal))
    OutputStr += str(name) + " : " + str(percentile) +"%  ("+ str(total) +")\n"

winner = max(candidatesTotal, key=candidatesTotal.get)

if winner is None:
    winner = ""

# winner
OutputStr += "\n----------------------------------------------------------------------"
OutputStr += "\n"
OutputStr += "\n Winner: " + (winner)
OutputStr += "\n"
OutputStr += "\n----------------------------------------------------------------------"

# 1) Output Report to terminal
print(OutputStr)

#2) Output Report to a text file
filename="Analysis/Results.txt"
with open(filename, 'w') as txtFile:
    txtFile.write(OutputStr)

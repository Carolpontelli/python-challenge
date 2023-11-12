# Python-challenge/PyBank

# import libraries
import os
import csv

# reading csv file
# assigning csv data to variables---------------------------------------------------------------------
# variable declarations and starting values
rowCount = 0
totalNumberOfMonths = 0
totalProfit = 0               #totalizing while looping

filename="C:/Users/anaca/Documents/python-challenge/PyBank/Resources/budget_data.csv" 
with open(filename, mode='r') as csvFile:
# creating a csv reader object
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        # create list for profit column
        profit=rows['Profit/Losses'] 
        totalProfit = totalProfit + int(profit)      
        rowCount += 1
totalNumberOfMonths = rowCount

# csv file to csv data matrix 
csvData = []
filename="C:/Users/anaca/Documents/python-challenge/PyBank/Resources/budget_data.csv" 
with open(filename) as csvfile:
# creating a csv reader object
    reader = csv.reader(csvfile) 
    for row in reader:          # each row is a list
        csvData.append(row)     # will be referring like csvData[row][col]

totalChangeProfit = 0
averageChangeProfit = 0
maxMonthlyChangeProfit = 0
minMonthlyChangeProfit = 0
for m in range(totalNumberOfMonths + 1): #range is +1 because of m starting from 0
    if(m > 1):
        currentMonthProfit  = int(csvData[m][1])
        previousMonthProfit = int(csvData[m-1][1])
        monthlyChangeProfit =currentMonthProfit - previousMonthProfit
        totalChangeProfit += monthlyChangeProfit
        # print(monthlyChangeProfit)                                    # temporary for testing each months change

        #find max
        if( monthlyChangeProfit > maxMonthlyChangeProfit):
            maxMonthlyChangeProfit = monthlyChangeProfit
            maxMonthName = str(csvData[m][0])
            # split string by '-' to change the format                  # date format is day-month      like 1-Jan
            parts = maxMonthName.split('-')                             # parts is a list with two data
            maxMonthName = parts[1] + '-' + parts[0]                    # now date is month-day         like Jan-1


        #find min
        if( monthlyChangeProfit < minMonthlyChangeProfit):
            minMonthlyChangeProfit = monthlyChangeProfit
            minMonthName = str(csvData[m][0])                           
            # split string by '-' to change the format                  # date format is day-month       like 1-Jan
            parts = minMonthName.split('-')                             # parts is a list with two data
            minMonthName = parts[1] + '-' + parts[0]                    # now date is month-day like     like Jan-1

numberOfChanges = rowCount-1 
averageChangeProfit = round(totalChangeProfit/numberOfChanges, 2)
# print(averageChangeProfit)                                            # temporary for testing average change

# Output Report to terminal
totalNumberOfMonths    = str(totalNumberOfMonths) 
total                  = '$'+str(totalProfit)
averageChangeProfit    = '$'+str(averageChangeProfit)
maxMonthlyChangeProfit = maxMonthName + ' ($'+ str(maxMonthlyChangeProfit) + ')'
minMonthlyChangeProfit = minMonthName + ' ($'+ str(minMonthlyChangeProfit) + ')'

# convert all output to a string, then send to: 1)print to terminal 2)export to a text file
outputStr = ''
outputStr += "----------------------------------------------------------------------"
outputStr += "\n          Python-challenge/PyBank                                     "
outputStr += "\n----------------------------------------------------------------------"
outputStr += "\n"
outputStr += "\n"
outputStr += "\n"
outputStr += "\n----------------------------------------------------------------------"
outputStr += "\n                        Financial Analysis                            "
outputStr += "\n----------------------------------------------------------------------"
outputStr += "\n"
outputStr += "\n Total Months                 : " + totalNumberOfMonths
outputStr += "\n"
outputStr += "\n"
outputStr += "\n Total                        : " + total
outputStr += "\n"
outputStr += "\n"
outputStr += "\n Average Change               : " + averageChangeProfit
outputStr += "\n"
outputStr += "\n"
outputStr += "\n Greatest Increase in Profits : " + maxMonthlyChangeProfit
outputStr += "\n"
outputStr += "\n"
outputStr += "\n Greatest Decrease in Profits : " + minMonthlyChangeProfit
outputStr += "\n"
outputStr += "\n----------------------------------------------------------------------"
outputStr += "\n"

# 1) Output Report to terminal
print(outputStr)

# 2) Output Report to a text file
filename="C:/Users/anaca/Documents/python-challenge/PyBank/Analysis/Financial Analysis.txt" 
with open(filename, 'w') as txtFile:
    txtFile.write(outputStr)
    
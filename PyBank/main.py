#module imports
import os
import csv

#compress path to csv file
path = '../Desktop/school stuff/pythonhw/python-challenge/PyBank/Resources/budget_data.csv'
  #path = 'Resources/budget_data.csv'
#open csv file as readonly and name
budget_data = open(path,'r')

#reader call and seperate file by comma
reader = csv.reader(budget_data, delimiter=',')

#csv header print and skip
csv_header = next(reader)
print(f"CSV Header: {csv_header}")

#variables
months = 0
rowadd = 0
totallist = []

#for loop thru file
for row in reader:
   #  months counter
   months = (months) + 1
   # pull values to rowadd value
   rowadd = row[1]
   #add rowvalue to list
   totallist.append(rowadd)
  
total = sum(totallist)
  #Print total months
print('Total # of months: ' + (str)(months))
  #Print Profit/loss total
print('Total Profit/Loss:$ ' + (str)(total))

#Average Profit/Loss
#average = Sum/len(totallist)
#print('Average of Profit/Loss:$ ' (str)average)


#sample code
# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

#workaround solution for windows
#if using \ use command
# .replace("\","/") at end of line
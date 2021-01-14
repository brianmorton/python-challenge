#module imports
import os
import csv
import shutil

#variables
months = 0
rowadd = 0
totallist = []
greatcomp = 0
lesscomp = 0



#compress path to csv file
path = '../Desktop/school stuff/pythonhw/python-challenge/PyBank/Resources/budget_data.csv'
  #path = 'Resources/budget_data.csv'
#open csv file as readonly and name
budget_data = open(path,'r')

#reader call and seperate file by comma
reader = csv.reader(budget_data, delimiter=',')

#csv header print and skip
csv_header = next(reader)




#for loop thru file
for row in reader:
   #  months counter
   months = (months) + 1

   # pull values to rowadd value
   rowadd = int(row[1])
   #add rowvalue to list
   totallist.append(rowadd)
    #greatest month if statement
   if (int(row[1]) >= greatcomp):
    greatcomp = int(row[1])
    greatmonth = row[0]
    #lowest month if statment
   if (int(row[1]) <= lesscomp):
    lesscomp = int(row[1])
    lessmonth = row[0]

total = sum(totallist)
  #Print total months
print('Total # of months: ' + (str)(months))
  #Print Profit/loss total
print('Total Profit/Loss:$ ' + (str)(total))
#Average Profit/Loss
average = (total)/(months)
print('Average of Profit/Loss:$ ' + (str)(average))
#Greatest amt print statment
print('Greatest amount of profit was ' + (str)(greatcomp) + ' in ' + (greatmonth))
#Greatest loss print statment
print('Greatest loss of profit was ' + (str)(lesscomp) + ' in ' + (lessmonth))

#Export results to txt file
analysispath = 'C:/Users/Brian Morton.000/Desktop/school stuff/pythonhw/python-challenge/PyBank/Resources/Analysis/analysis.txt'
currentpath = 'C:/Users/Brian Morton.000/upenn-phi-data-pt-12-2020-u-c/analysis.txt'
analysis = "analysis.txt"
#os.path.join(path,file_name)
    
#adding above print statements as writes
analysisw = open(analysis, "w")
analysisw.write('Total # of months: ' + (str)(months))
analysisw.write('Total Profit/Loss:$ ' + (str)(total))
analysisw.write('Average of Profit/Loss:$ ' + (str)(average))
analysisw.write('Greatest amount of profit was ' + (str)(greatcomp) + ' in ' + (greatmonth))
analysisw.write('Greatest loss of profit was ' + (str)(lesscomp) + ' in ' + (lessmonth))

#move file
os.rename(currentpath, analysispath)


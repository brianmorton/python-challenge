#module imports
import os
import csv

#compress path to csv file
path = os.path.join('Resources', 'budget_data.csv').replace("\\","/")

#open csv file as readonly and name
budget_data = open(path,'r')

#reader call and seperate file by comma
reader = csv.reader(budget_data, delimiter=',')

#csv header print and skip
csv_header = next(reader)
print(f"CSV Header: {csv_header}")

#for loop thru file
for row in reader:
   # print statement of file to see if working
  print(row)
    






#sample code
# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

#workaround solution for windows
#if using \\ use command
# .replace("\\","/") at end of line


#'..', 'Pybank',
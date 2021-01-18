#Pypoll
import os
import csv

path = os.path.join('Resources','Election_Data.csv')

election_data = open(path,'r')
reader = csv.reader(election_data, delimiter=',')

#variables
can1 = 'x'
can2 = 'x'
can3 = 'x'
can4 = 'x'

can1total = 0
can2total = 0
can3total = 0
can4total = 0
Totalvotes = 0

Compwin1 = 0
Compname1 = ''
Compwin2 = 0
Compname2 = ''
FinalName = ''
Finaltotal = 0

#grab names
csv_header = next(reader)

for row in reader:
        #assign checker name for comparsion
        checker = (row[2])
      #first if add match and next statement
        if  checker == can1:
                can1total+=1
                next
                #else if hits x to assign and next to continue loop
        elif can1 == 'x':
                can1 = checker
                can1total+=1

        elif  checker == can2:
                can2total+=1
                next
        elif can2 == 'x':
                can2 = checker
                can2total+=1

        elif  checker == can3:
                can3total+=1
                next
        elif can3 == 'x':
                can3 = checker
                can3total+=1

        elif  checker == can4:
                can4total+=1
                next
        elif can4 == 'x':
                can4 = checker   
                can4total+=1    

        
        
     #Add votes for total   
Totalvotes = (can1total + can2total + can3total + can4total)

#percentage calculator
can1per = (can1total/Totalvotes) * 100
can2per = (can2total/Totalvotes) * 100
can3per = (can3total/Totalvotes) * 100
can4per = (can4total/Totalvotes) * 100




#Vote total comparsion
if can1total > can2total:
        Compwin1 = can1total
        Compname1 = can1
elif can1total < can2total:
        Comwin1 = can2total
        Compname1 = can2

if can3total > can4total:
        Compwin2 = can3total
        Compname2 = can3
elif can3total < can4total:
        Comwin2 = can4total
        Compname2 = can4        

if Compwin1 > Compwin2:
        Finaltotal = Compwin1
        Finalname = Compname1
elif Compwin1 < Compwin2:
        Finaltotal = Compwin2
        Finalname = Compname2


print(Compname2)
print(Compwin2)
#print statements
print('The total number of votes cast was: ' + str(Totalvotes))
print ('Candidate ' + (can1) + ' won ' + str(can1total) + ' votes with ' + str(can1per) + '% of the vote.')
print ('Candidate ' + (can2) + ' won ' + str(can2total) + ' votes with ' + str(can2per) + '% of the vote.')
print ('Candidate ' + (can3) + ' won ' + str(can3total) + ' votes with ' + str(can3per) + '% of the vote.')
print ('Candidate ' + (can4) + ' won ' + str(can4total) + ' votes with ' + str(can4per) + '% of the vote.')
print ('Candidate ' + (Finalname) + ' has won the election!')


#Export 
analysispath = os.path.join('Analysis','Analysis.txt')
analysis_data = open(analysispath,'w')

analysis_data.write('The total number of votes cast was: ' + str(Totalvotes))
analysis_data.write('Candidate ' + (can1) + ' won ' + str(can1total) + ' votes with ' + str(can1per) + '% of the vote.')
analysis_data.write('Candidate ' + (can2) + ' won ' + str(can2total) + ' votes with ' + str(can2per) + '% of the vote.')
analysis_data.write('Candidate ' + (can3) + ' won ' + str(can3total) + ' votes with ' + str(can3per) + '% of the vote.')
analysis_data.write('Candidate ' + (can4) + ' won ' + str(can4total) + ' votes with ' + str(can4per) + '% of the vote.')
analysis_data.write ('Candidate ' + (Finalname) + ' has won the election!')

import csv
import datetime
import string
with open('employee_data1.csv', newline='') as csvfile:
    employee_table = csv.reader(csvfile, delimiter=',')
    next(employee_table)
    
    for row in employee_table :
        date = datetime.datetime.strptime(row[2], "%Y-%m-%d")
        
    #for row in employee_table :
        splitname=(row[1].split(" "))
        split_Fname=splitname[0]
        split_Lname=splitname[1]
        fieldSSN=row[3]
        string_length=len(fieldSSN)
        lastfour=string_length-4
        value=fieldSSN[lastfour:]
        final_SSN="***-**-" + value
        #print(final_SSN)

        new_row= (row[0]+","+split_Fname+","+split_Lname+","+new_DOB+","+final_SSN)
        print(new_row)
    


##################################################################################
# Author: Apoorva Anwekar
# Solution for Homework #3 PyBank.
################################################################################## 

import csv
#open a file
with open('budget_data_1.csv', newline='') as csvfile:
    #read the  file with csv
    csvtable = csv.reader(csvfile, delimiter=',')
    #skip the header row
    next(csvtable)
    #initializing a counter for counting total revenue
    total = 0
    #initializing a counter for counting number of months
    row_count = 0
    #initializing a variable to store revenue for previous month
    prev_month_revenue = 0
    #initializing a variable to track Greatest Increase in Revenue
    gretest_revenue_inc = 0
    #initializing a variable to track Greatest Derease in Revenue
    gretest_revenue_dec = 0
    #initializing a counter to calculate total change in revenue
    total_revenue_change = 0
    #looping through each row in the table
    for row in csvtable:
        #calculate total revenue
        total += int(row[1])
        #increment the counter by 1 every iteration
        row_count += 1
        #excluding the first month as there will be no revenue change 
        if prev_month_revenue != 0:
            #calculate revenue change for current month
            revenue_change=int(row[1])-prev_month_revenue
            #calculate total revenue change
            total_revenue_change+=revenue_change
            #comparing the current change in value to the previous greatest increase in revenue
            if revenue_change > gretest_revenue_inc:
                #update the greatest increase in revenue to current month
                gretest_revenue_inc = revenue_change
                gretest_revenue_incmonth = row[0]
            #comparing the current change in value to the previous greatest decrease in revenue
            if revenue_change < gretest_revenue_dec:
                #update the greatest decrease in revenue to current month
                gretest_revenue_dec = revenue_change
                gretest_revenue_decmonth = row[0]
        #assigning the value of current revenue to the variable for using it as previous revenue
        prev_month_revenue=int(row[1])
#write to terminal
print("Financial Analysis")
print("-------------------------")
print("Total Months: $", row_count)  
print("Total Revenue: $", total)
print("Average Revenue Change: $", round(total_revenue_change/ (row_count - 1),0))
print("Greatest Increase in Revenue: ", gretest_revenue_incmonth, "($", gretest_revenue_inc, ")")
print("Greatest Decrease in Revenue: ", gretest_revenue_decmonth, "($", gretest_revenue_dec, ")")
#write to file
with open('results.txt', 'w') as results:
    #printing all the values to the given format
    print("Financial Analysis", file = results)
    print("-------------------------", file = results)
    print("Total Months: $", row_count, file = results)  
    print("Total Revenue: $", total, file = results)
    print("Average Revenue Change: $", round(total_revenue_change/ (row_count - 1),0), file = results)
    print("Greatest Increase in Revenue: ", gretest_revenue_incmonth, "($", gretest_revenue_inc, ")", file = results)
    print("Greatest Decrease in Revenue: ", gretest_revenue_decmonth, "($", gretest_revenue_dec, ")", file = results)
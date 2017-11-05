##################################################################################
# Author: Apoorva Anwekar
# Solution for Homework #3 PyPoll.
################################################################################## 
import csv
#open a file
with open('election_data_2.csv', newline='') as csvfile:
#read the  file with csv
    election_data = csv.reader(csvfile, delimiter=',')
    #read the  file with csv    
    next(election_data)
    #creating an empty dictionary
    mydict = {}
    #initializing a counter for counting total votes
    count = 0
    #initializing a counter for storing maximum number of votes per candidate
    max_votes = 0
    #looping through each row in the table
    for row in election_data :
        #increment the counter by 1 every iteration
        count +=1
        #storing a value in candidate per iteration for row[2]
        candidate = row[2]
        #check for condition
        if candidate in mydict:
            mydict[candidate] += 1
        else:
            mydict[candidate] = 1
    #Print the header string
    print("Election Results")
    print( "-------------------------")
    print("Total Votes: " + str(count))
    print("-------------------------")

    for  candidate in mydict.keys() :
         count_of_votes=mydict[candidate]
         #calculating the percentage and rounding of thr result to 2 places of decimal
         percentage=round((count_of_votes/count)*100.00,2)
         #print the result 
         print (candidate + (": ") + str(percentage) +  ("% (")  + str(count_of_votes) + ")")
         #check for condition to find out winner by finding the max votes
         if count_of_votes > max_votes :
             max_votes=count_of_votes
             winner=candidate
    print ("-------------------------")
    print("Winner: "+ winner )
    print ("-------------------------")
    

import os
import csv
from collections import Counter

csvpath = os.path.join( "/Users/Danie/Desktop/Python1/", "election_data.csv")
votes = 0
uniques = []
ballots = []
ballotsc = []
words3 = []
words4 =[]
percentages = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header=next(csvfile)

    for row in csvreader:
        votes = votes + 1
        ballots = str(row[2])
        ballotsc.append(ballots) 
        if row[2] not in uniques:
            uniques.append(row[2])
     
    words = Counter(ballotsc).keys() # equals to list(set(words))
    words2 = Counter(ballotsc).values() # counts the elements' frequency
    for elements in words2:
        words4.append(int(elements))
        words3.append(float(elements)/float(votes))
        percentages.append((float(elements)/float(votes))*100.0)
    
    roundp = ['%.4f'% num for num in percentages]
   

    
        
    #print(uniques)
    #print(roundp)
    #print('%.4f' % roundp[])
    #print(votes)
    #print(words)
    #print(words2)
    #print(words3)
    #print(percentages)
    #print(roundp)
    #print(words4)
    #print(dictionary)
    #combined_dict= dict(zip(uniques,roundp))
    #print(combined_dict)
    #combined_dict2=dict(zip(combined_dict))
    #print(combined_dict2)

    print("----------------------------------------------------")

    print("Election Results")

    print("----------------------------------------------------")

    print("Total Votes: " + str(votes))

    print("----------------------------------------------------")

    print((str(uniques[0])) +":"+ str(roundp [0]) +"%" + "(" + str(words4[0])+")" )
    print((str(uniques[1])) +":"+ str(roundp [1]) +"%" + "(" + str(words4[1])+")" )
    print((str(uniques[2])) +":"+ str(roundp [2]) +"%" + "(" + str(words4[2])+")" )
    print((str(uniques[3])) +":"+ str(roundp [3]) +"%" + "(" + str(words4[3])+")" )

    print("----------------------------------------------------")

    print("winner : "+ str(uniques[0]))



    




    
    
    

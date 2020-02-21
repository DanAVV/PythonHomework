
import os
import csv
from statistics import mean

csvpath = os.path.join( "/Users/Danie/Desktop/Python1/", "budget_data.csv")

months = 0
netamount = 0 
amountbefore = 0
final_profit = 0
change = []
date = []
total_change_profits = 0
highest=0
lowest=100000000000000
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header=next(csvfile)
    
    


    for bank_data in csvreader:
        profit_loss = float(bank_data[1])
    
    
        #for i in range(len(profit_loss)-1)

        months = months+1
        date.append(bank_data[0])
        netamount = netamount + profit_loss
        initial_profit = int(bank_data[1])
        monthly_change_profits = final_profit - initial_profit
        change.append(monthly_change_profits)
        #print(monthly_change_profits)
        final_profit = initial_profit
        
        total_change_profits = total_change_profits + monthly_change_profits

        Averagetotalchange = total_change_profits/months
        #print(Averagetotalchange)



        if monthly_change_profits >= highest:
            highest=monthly_change_profits
        if monthly_change_profits <= lowest:
            lowest = monthly_change_profits


    print("--------------------")

    print("Financial analysis")

    print("-------------------")

    print("Total Months : " + str(months))
    print("Total : $" + str(netamount))
    print("average change : $" + str(Averagetotalchange))
    print("Greatest Increase in profits : $" + str(highest))
    print("Greatest Decrease in profits : $" + str(lowest))
    #print(months)
    #print(netamount)
    #print(Averagetotalchange)
    #print(highest)
    #print(lowest)


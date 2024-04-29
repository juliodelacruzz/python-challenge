#importing modules
import os
import csv


#defining csv path 
csvpath = os.path.join("Starter_Code/Starter_Code/PyBank/Resources/budget_data.csv")

total_months = 0 #this is our counter, which will be used in our for loop
total_profit_losses = 0 #another counter variable
previous_profit_losses = None
change_profit_loss = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]



# Open and reading the csv file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Skipping the header row

    for row in csvreader:

        #gettting total months
        total_months += 1 #our previous counter variable, which we be used to count the months with each iteration

        #getting the net total of profit/losses
        #Values within csv files are usually read in strings, so we must convert to integers in order to get the total
        #row[1] is directly accessing data from the rows and changing them into integers. [Jan-10,1088983], returns 1088983
        current_profit_losses = int(row[1])
        total_profit_losses += current_profit_losses 

        #changes in Profit/Losses
        if previous_profit_losses is not None: #initially, there is no previous month profit/loss to compare
            change = current_profit_losses - previous_profit_losses
            change_profit_loss.append(change)
        previous_profit_losses = current_profit_losses

#average changes in profit loss
average_change = sum(change_profit_loss) / len(change_profit_loss)


if change_profit_loss:  
    greatest_increase = ["Max Change", max(change_profit_loss)]
    greatest_decrease = ["Min Change", min(change_profit_loss)]



# Prepare output results
    results_txt = (
        "Financial Analysis\n"
    "-------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total Profit/Losses: ${total_profit_losses}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: ${greatest_increase[1]}\n"
        f"Greatest Decrease in Profits: ${greatest_decrease[1]}\n"
    )

    print(results_txt)


pyBank_txt = 'Starter_Code/Starter_Code/PyBank/analysis/pyBank.txt'
with open(pyBank_txt, 'w') as textfile:
        textfile.write(results_txt)

#Importing necessary CSV file and Operations
import os
import csv
budget_data_csv = os.path.join("Resources", "budget_data.csv")
#Defining variables as arrays and integers
total_months = []
net_profit_losses = 0
change_profit_losses = []
avg_of_change = 0
greatest_increase = ["",0]
greatest_decrease = ["",0]
#Open the CSV File and Created necessary variables to read the File
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader, None)
    first_row = next(csvreader, None)
    total_months.append(first_row[0])
    net_profit_losses_row = int(first_row[1])
    net_profit_losses += net_profit_losses_row
    previous_row = int(first_row[1])
#Begin looping over data for retrieval
    for row in csvreader:
        total_months.append(row[0])
        net_profit_losses_row = int(row[1])
        change = int(row[1]) - previous_row
        net_profit_losses += net_profit_losses_row
        change_profit_losses.append(int(row[1])-previous_row)
        previous_row = int(row[1])
        if change > greatest_increase[1]:
            greatest_increase[1] = change
            greatest_increase[0] = row[0]
        if change < greatest_decrease[1]:
            greatest_decrease[1] = change
            greatest_decrease[0] = row[0]
avg_of_change = round(sum(change_profit_losses) / len(change_profit_losses), 2)
#Output data via Print Statements
print("                  ")
print("Financial Analysis")
print("---------------------------------------")
print("Total Months" + ": " + str(len(total_months)))
print("Total" + ": $" + str(net_profit_losses))
print("Average Change" + ": $" + str(avg_of_change))
print("Greatest Increase in Profits: " + str(greatest_increase[0]) + " $(" + str(greatest_increase[1]) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + " $(" + str(greatest_decrease[1]) + ")")



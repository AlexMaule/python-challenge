import os
import csv

budget_path = os.path.join("..","PyBank","Resources","budget_data.csv")


with open(budget_path,'r') as rfile:
    csv_reader = csv.reader(rfile,delimiter = ",")

    header = next(csv_reader) # don't want to include the header

    row_count = 0 
    total = 0
    greatest_increase = 0
    greatest_decrease = 0
    total_change = 0
    data = []

    for row in csv_reader:

        row_count += 1 # Number of months
        total += int(row[1]) # Total Amount of Profit/Losses

        date = row[0]
        profit_loss = int(row[1])
        data.append([date,profit_loss])

    for i in range(len(data)-1):
        difference = data[i+1][1] - data[i][1]
        total_change += difference # Total Change
        if difference > 0:
            if greatest_increase < difference:
                greatest_increase = difference # Greatest Increase
                greatest_increase_date = data[i+1][0] # Date of the Greatest Increase
        else:
            if greatest_decrease > difference:
                greatest_decrease = difference # Greatest Decrease
                greatest_decrease_date = data[i+1][0] # Date of the Greatest Decrease

    average_change = total_change/(row_count - 1) # Average Change

    write_path = os.path.join("..","PyBank","Analysis","financial_analysis.txt")
    with open(write_path,'w') as wfile:

        wfile.write("Financial Analysis")
        wfile.write("\n-------------------------------------")
        wfile.write("\nTotal Months: " + str(row_count))
        wfile.write("\nTotal: $" + str(total))
        wfile.write("\nAverage Change: $" + str(round(average_change,2)))
        wfile.write("\nGreatest Increase in Profits " + str(greatest_increase_date) + " (" + str(greatest_increase) + ")")
        wfile.write("\nGreatest Decrease in Profits: " + str(greatest_decrease_date) + " (" + str(greatest_decrease) + ")")

    rfile = open(write_path,'r')
    print(rfile.read())
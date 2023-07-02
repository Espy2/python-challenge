# Importing modules
import os
import csv

# Establishing File Path
csvpath = os.path.join('Resources', 'budget_data.csv')

#Open the CSV file
with open(csvpath) as csvfile : 

    csvreader = csv.reader(csvfile)

    # Skip the header
    next(csvreader)

    #Assign variables for for loop
    row_count = 0
    previous_value = 0
    total_change = 0
    net_total= 0
    greatest_increase = 0
    greatest_increase_month = ' '
    greatest_decrease = 0
    greatest_decrease_month = ' '


    # Loop through each row
    for row in csvreader : 
        #Count the number of rows(Months)
        row_count += 1
        #Calculate the net total
        current_value = int(row[1])
        net_total += current_value

        # Calculating change 
        if row_count >1 :
            change = current_value - previous_value
            total_change += change

            # tracking greatest increase
            if change > greatest_increase: 
                greatest_increase = change
                greatest_increase_month = row[0]
            
            # tracking greatest decrease
            if change < greatest_decrease :
                greatest_decrease = change
                greatest_decrease_month = row[0]

            
        
        previous_value = current_value

    # Loop through each row and count the number o

average_change = total_change / (row_count - 1)

# Printing totals
print( "Number of Months: ", row_count)

print("Total: ", net_total)

print("Average change: ", average_change)

print('Greatest Increase in Profits: ', greatest_increase_month, greatest_increase)

print('Greatest decrease in Profits: ', greatest_decrease_month, greatest_decrease)



   



import csv

# initialize variables and open csv files to read and write

sales = open("sales.csv", "r")
csv_file = csv.reader(sales)
outfile = open("salesreport.csv", "w")
next(csv_file)
full_expense = 0
last_sales_id = -1
outfile.write("Sales ID, Total")

#this for loop should check if the entry is a repeat, and fork based on if it is a repeat or not
for record in csv_file:
    #record the current entries
    sales_id = record[0]
    current_expense = float(record[3]) + float(record[4]) + float(record[5])
    if sales_id != last_sales_id:
        #this ensures that the first entry doesn't print a blank
        if last_sales_id == -1: 
            full_expense = current_expense
        else:
            #if the current entry is NOT a repeat, and is NOT the first entry, it will print the total to the file    
            writer = "\n{}, {}".format(last_sales_id, round(full_expense, 2))
            outfile.write(writer)
            full_expense = current_expense
            
    else:
        #if the current entry IS a repeat, then add the current expense to the total expense
        full_expense += current_expense
    last_sales_id = sales_id

#since the way I print the files depends on still being in the for loop to print a previous file,
#I print the last file outside of the for loop
writer = "\n{}, {}".format(last_sales_id, round(full_expense, 2))
outfile.write(writer)

outfile.close()
sales.close()
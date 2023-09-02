import csv

#initialize variables and open files
customers = open("customers.csv", "r")
csv_file = csv.reader(customers)
outfile = open("customer_country.csv", "w")
next(csv_file)

for record in csv_file:
    #finds the data in the file
    first_name = record[1]
    last_name = record[2]
    country = record[4]
    writer = "{}, {}, {}\n".format(first_name, last_name, country)
    #writes the data stored in writer, and makes a new line
    outfile.write(writer)
outfile.close()
customers.close()


# customers = open("customers.csv", "r")

# csv_file = csv.reader(customers)

# next(csv_file)

# for record in csv_file:
#     print(record)
#     print(f'First Name: {record[1]}')
#     print(f'Last Name: {record[2]}')
#     input()

#     outfile = open("philosophers.txt", "a")
#     outfile.write("Sidney Wilhite :D\n")
#     outfile.close()
#     print("philosophers.txt")
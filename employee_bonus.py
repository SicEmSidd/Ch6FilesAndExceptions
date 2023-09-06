import csv

#initialize variables and open files
employees = open("EmployeePay.csv", "r")
csv_file = csv.reader(employees)
next(csv_file)
menu_input = 0

#prints employee records, paused by an input so it doesn't flood the screen
while menu_input != "close":
    for record in csv_file:
        if menu_input == "close":
            break
        print(f"Employee Name: {record[1]} {record[2]}")
        print(f"Employee Salary: ${float(record[3]):10,.2f}")
        #the bonus is calculated by the percent times the salary
        print(f"Employee Bonus:  ${round(float(record[4])*float(record[3])):10,.2f}")
        print(f"Employee Pay:    $ {round(float(record[4])*float(record[3])+float(record[3])):1,.2f}")
        menu_input = str(input("Press any button to continue, or type 'close' to exit the program. "))
    break
print("Thanks for using my program!")
employees.close()
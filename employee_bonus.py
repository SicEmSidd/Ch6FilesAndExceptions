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
        print("Employee Name: " +record[1] + " " + record[2], sep = '')
        print("Employee Salary: $" +record[3], sep = '')
        #the bonus is calculated by the percent times the salary
        print("Employee Bonus: $" +str(round(float(record[4])*float(record[3]))), sep = '')
        menu_input = str(input("Press any button to continue, or type 'close' to exit the program. "))
print("Thanks for using my program!")
employees.close()
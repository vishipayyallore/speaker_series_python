""" Program to demonstrate Basics of Input/Output
"""

# Importing Modules
import datetime


def get_show_employee_details():

    # Calculating the date
    todays_date = datetime.datetime.now()
    today = todays_date.strftime('%c')

    # Accepting Inputs from User
    name = input("Enter Your Name: ")
    employee_id = int(input("Enter Employee Id: "))
    salary = float(input("Enter Salary: "))
    is_manager = bool(int(input("Enter Manager Status {1/0}: ")))

    # Displaying the output
    print("====================================================")
    print(f"Employee Details | Date: {today} |")
    print("====================================================")
    print(f"\tName: {name}")
    print(f"\tId: {employee_id}")
    print(f"\tSalary: {salary}")
    print(f"\tIs Manager: {is_manager}")
    print("----------------------------------------------------")


def main():
    get_show_employee_details()


main()




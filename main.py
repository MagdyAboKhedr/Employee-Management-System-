import employee_data
import authentication
import operations

#   Employee Managment System:
#     Made by: Magdy AboKhedr
#     Date: 7/12/2024

    


print("Welcome to Employee Managment System\n")
print("Please login to continue: \n")


if __name__ == '__main__':
    login_status = authentication.authFunc()
    while login_status == True:
        print("Select an option: \n")
        print("1. Display Employee information \n")
        print("2. Calculate Bonus \n")
        print("3. Calculate Discount \n")
        print("4. Remind Legal Holidays \n")
        print("5. Add new employee \n")
        print("6. Exit \n")
        choice = input("Enter your choice: ")

        if choice == '1':
            operations.display_info()
        if choice == '2':
            operations.calc_bonus()
        if choice == '3':
            operations.calc_disc()
        if choice == '4':
            operations.legal_holi()
        if choice == '5':
            operations.add_employee()
        if choice == '6':
            print("Thank you for using employee managment system. Goodbye!")
            break
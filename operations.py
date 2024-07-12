import employee_data

def display_info():
    local_id = input("Enter Employee ID: ")
    for target_employee in employee_data.data:
        if target_employee.get('ID') == local_id:
            employee_details = {k: v for k, v in target_employee.items() if k != 'pw'}
            for key, value in employee_details.items():
                print(f"{key}: {value}")


def calc_bonus():
    local_id = input("Enter Employee ID: ")
    for target_employee in employee_data.data:
        if target_employee.get('ID') == local_id:
           bonus = int(target_employee.get('Salary')) * 0.1
           print("Bonus = ", bonus)

def calc_disc():
    local_id = input("Enter Employee ID: ")
    for target_employee in employee_data.data:
        if target_employee.get('ID') == local_id:
           disc = int(target_employee.get('Salary')) * 0.05
           print("Discount = ", disc)

def legal_holi():
    local_id = input("Enter Employee ID: ")
    for target_employee in employee_data.data:
        if target_employee.get('ID') == local_id:
           days_rem = 21 - int(target_employee.get('Days of Absence')) 
           print("Discount = ", days_rem)


def add_employee():
    ID = input("Enter ID: ")
    Name = input("Enter Name: ")
    Department = input("Enter Department: ")
    Salary = input("Enter Salary: ")
    pw = input("Enter password: ")
    Days_of_Absence = input("Enter Days of Absence: ")
    
    new_employee = {
        'ID': ID,
        'Name': Name,
        'Department': Department,
        'Salary': Salary,
        'pw': pw,
        'Days of Absence': Days_of_Absence
    }
    employee_data.data.append(new_employee)



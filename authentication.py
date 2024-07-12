import pwinput
import employee_data

def authFunc():
    local_id = input("Enter your employee ID: ")
    local_pw_count = 0
    
    for target_employee in employee_data.data:
        if target_employee.get('ID') == local_id:
            while local_pw_count < 3:
                local_pw = pwinput.pwinput(prompt='Enter your password: ')
                if target_employee.get('pw') == local_pw:
                    print("Login Successful!")
                    return True
                else:
                    local_pw_count += 1
                    print(f"Incorrect Password, attempt {local_pw_count} / 3")
            print("Login failed")
            return
    
    print("Employee ID not found")



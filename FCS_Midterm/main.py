from read_text import get_names
from menus import admin_menu
from menus import employee_menu
path = "Employees.txt"
data = get_names(path)
count = 0

correct_username = False
while count < 5:#O(n)
    login_username=input("Please enter your Username")
    login_password=input("Please enter your Password")
    if login_username == "Admin" and login_password == "Admin123123":
        new_employees = []
        for i in range(len(data)):
            new_employee = ",".join(str(value) for value in data[i].values())
            new_employees.append(new_employee)
        string_new_employee = "".join(str(value) for value in new_employees)
        print("Admin Menu")
        admin_exit = False
        while admin_exit == False:
            admin_exit, string_new_employee = admin_menu(data,string_new_employee)
        count = 0

    elif login_username != "Admin" and login_password == "" and login_username != "":
        for i in data:
            if login_username == i["username"][1:]:
                employee_exit = False
                while employee_exit == False:
                    employee_menu(data,login_username)
                    employee_exit = employee_menu(data,login_username)
                    correct_username = True
                    count = 0
                    break
        if correct_username == False:
            count += 1
    else:
        count +=1
        if count == 5:
            print("You have been blocked")








from read_text import get_names
from menus import admin_menu
from menus import employee_menu
path = "Employees.txt"
data = get_names(path)
count = 0

correct_username = False
while count < 5:
    login_username=input("Please enter your Username")
    login_password=input("Please enter your Password")
    if login_username == "Admin" and login_password == "Admin123123":
        print("Admin Menu")
        admin_exit = False
        while admin_exit == False:
            admin_exit = admin_menu(data)
        break
    elif login_username != "Admin" and login_password == "" and login_username != "":
        for i in data:
            if login_username == i["username"][1:]:
                employee_menu(data,login_username)
                correct_username = True
                break
        if correct_username == True:
            break
        else:
            count += 1
            print(count)
    else:
        count +=1
        if count == 5:
            print("You have been blocked")








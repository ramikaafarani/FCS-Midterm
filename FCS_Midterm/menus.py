# https://sparkbyexamples.com/python/how-to-append-to-a-file-in-python/(how to append to file txt)
# https://www.tutorialspoint.com/how-to-add-leading-zeros-to-a-number-in-python#:~:text=zfill()%20method,that%20will%20come%20as%20output.(Add 00 to the employee id to be matching format)
# https://bobbyhadz.com/blog/python-join-values-of-dictionary (join values in dictionary into a string with commas )
# https://www.programiz.com/python-programming/datetime (sort date)
# https://levelup.gitconnected.com/remove-whitespaces-from-strings-in-python-c5ee612ee9dc(remove spaces from the date)
# https://www.pythontutorial.net/python-basics/python-write-text-file/ (how to write to a txt file)
#https://www.geeksforgeeks.org/get-current-timestamp-using-python/(TimeStamp)
# https://bobbyhadz.com/blog/python-convert-comma-separated-string-to-dictionary#:~:text=To%20convert%20a%20dictionary%20to%20a%20comma%2Dseparated%20string%3A&text=keys%20or%20values.-,Use%20the%20str.,values%20with%20a%20comma%20separator.(convert dictionary into a string with comma's)
from datetime import datetime
def admin_menu(data):
    new_employees = []
    for i in range(len(data)):
        new_employee = ",".join(str(value) for value in data[i].values())
        new_employees.append(new_employee)
    string_new_employee = "".join(str(value) for value in new_employees)
    print(
        "1. Display Statistics\n" + "2. Add an Employee\n" + "3. Display all Employees\n" + "4. Change Employee’s Salary\n" + "5. Remove Employee\n" + "6. Raise Employee’s Salary\n" + "7. Exit\n")
    admin_input = int(input("Please Choose which option you want"))
    if admin_input == 1:
        male_count = 0
        female_count = 0
        for i in data:
            if i["gender"][1:] == "male":
                male_count += 1
            elif i["gender"][1:] == "female":
                female_count += 1
        print("Display Statistics")
        print("Number of Male's are",male_count ,"and Female's", female_count)
        return False
    elif admin_input == 2:
        last_id = data[-1]["id"][4:]
        new_numberofid = int(last_id) + 1
        new_id = str(new_numberofid).zfill(3)
        new_id = "emp" + str(new_id)
        print(" Add an Employee")
        username_input = input("Please enter employ New Username")
        joining_date_input = int(input("Please enter Joining Date"))
        gender_input = input("Please enter Gender")
        salary_input = int(input("Please enter Salary"))
        new_employee_info = {"id": new_id, "username": username_input, "date": str(joining_date_input), "gender": gender_input, "salary": str(salary_input)}
        string_new_employee = ", ".join(new_employee_info.values())
        return False

        # with open('Employees.txt', 'a') as f:
        #     f.write("\n" + new_employee)
    elif admin_input == 3:
        date_list = []
        for i in data:
            x = i['date']
            date_list.append(str.lstrip(x))

        date_list.sort(key=lambda date: datetime.strptime(date, "%Y%m%d"))
        new_sorted_dictionary = []
        for i in date_list:
            for x in data:
                if i == x['date'][1:]:
                    new_sorted_dictionary.append(x)
        for employee in data:
            employee = ",".join(employee.values())
            print("Display all Employees")
            print(employee)
        return False
    elif admin_input == 4:
        print("Change Employee’s Salary")
        input_id = input("Please input id")
        input_salary = input("Please input the new salary")
        for i in range(len(data) - 1):
            if input_id == data[i]['id']:
                data[i]['salary'] = str(input_salary) + "\n"
                list_new_employee = []
                for i in range(len(data)):
                    new_employee = ",".join(str(value) for value in data[i].values())
                    list_new_employee.append(new_employee)
                string_new_employee = "".join(str(value) for value in list_new_employee)
                # with open('Employees.txt', 'w') as f:
                #     f.write(str(string_new_employee))
                break
            else:
                if i == len(data) - 1:
                    print("Your id is wrong")
        return False
    elif admin_input == 5:
        print("Remove Employee")
        input_id = input("Please enter the ID you want to remove")
        list_new_employee = []
        for i in range(len(data)):
            if input_id == data[i]['id']:
                del data[i]
                for x in range(len(data)):
                    new_employee = ",".join(str(value) for value in data[x].values())
                    list_new_employee.append(new_employee)
                string_new_employee = "".join(str(value) for value in list_new_employee)
                # with open('Employees.txt', 'w') as f:
                #     f.write(str(string_new_employee))
                break
            else:
                if i == len(data) - 1:
                    print("Your id is wrong")
        return False
    elif admin_input == 6:
        print("Raise Employee’s Salary")
        input_id = input("Please input id")
        input_percentage = input("Please input the percentage of the raise")
        for i in range(len(data)):
            if input_id == data[i]['id']:
                x = data[i]['salary']
                x = float(x) + (float(x) * (float(input_percentage) / 100))
                data[i]['salary'] = str(x) + "\n"
                list_new_employee = []
                for i in range(len(data)):
                    new_employee = ",".join(str(value) for value in data[i].values())
                    list_new_employee.append(new_employee)
                string_new_employee = "".join(str(value) for value in list_new_employee)
                # with open('Employees.txt', 'w') as f:
                #     f.write(str(string_new_employee))
                break
            else:
                if i == len(data)-1:
                    print("Your id is wrong")
        return False
    elif admin_input == 7:
        with open('Employees.txt', 'w') as f:
            f.write(str(string_new_employee))
        return True
def employee_menu(data,loginusername):
    for i in data:
        if loginusername == i['username'][1:]:
            if i['gender'][1:] == 'male':
                gender = "Mr."
            else:
                gender = "Ms."
            name = i['username'][1:]
            print("Hi", gender, name.capitalize())
            print("1. Check my Salary \n" + "2. Exit\n")
            user_input = int(input("Please Choose which option you want"))
            if user_input == 1:
                print("Your salary is" +i['salary'])
            elif user_input == 2:
                ct = datetime.now()
                timestamp = ct.timestamp()
                with open('Timestamps.txt', 'a') as f:
                    f.write(str(name.capitalize()) + " logged in at " + str(timestamp) +"\n")
            break

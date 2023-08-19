# https://sparkbyexamples.com/python/how-to-append-to-a-file-in-python/(how to append to file txt)
# https://www.tutorialspoint.com/how-to-add-leading-zeros-to-a-number-in-python#:~:text=zfill()%20method,that%20will%20come%20as%20output.(Add 00 to the employee id to be matching format)
# https://www.geeksforgeeks.org/python-convert-dictionary-object-into-string/ (convert dictionary into string)
import json


def admin_menu(data):
    admin_input = int(input("Please Choose which option you want"))

    if admin_input == 1:
        male_count = 0
        female_count = 0
        for i in data:
            if i["gender"] == "male":
                male_count += 1
            elif i["gender"] == "female":
                female_count += 1
        print("Display Statistics")
        print("Number of Male's are",male_count ,"and Female's", female_count)
    elif admin_input == 2:
        last_id = data[-1]["id"][4:]
        new_numberofid = int(last_id) + 1
        new_id = str(new_numberofid).zfill(3)
        new_id = "emp" + str(new_id)
        print(new_id)
        username_input = input("Please enter employ New Username")
        joining_date_input = int(input("Please enter Joining Date"))
        gender_input = input("Please enter Gender")
        salary_input = input("Please enter Salary")
        new_employee = {"id": new_id, "username": username_input, "date": joining_date_input, "gender": gender_input, "salary": salary_input}
        new_employee = json.dumps(new_employee)
        with open('Employess.txt', 'a') as f:
            f.write(new_employee)
    # elif admin_input == 3:
    # elif admin_input == 4:
    # elif admin_input == 5:
    # elif admin_input == 6:
    # elif admin_input == 7:
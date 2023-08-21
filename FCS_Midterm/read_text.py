# https://www.pythontutorial.net/python-basics/python-read-text-file/ (Used to read a file)
# https://www.w3schools.com/python/ref_string_split.asp (Used to split the string into list)
# https://www.w3schools.com/python/ref_file_readlines.asp#:~:text=The%20readlines()%20method%20returns,no%20more%20lines%20are%20returned (what does readline do)
def get_names(path):#O(n)
    with open(path) as f:
        employees = f.readlines()
    data = []
    for employee in employees:
        employees_split = employee.split(",")
        id, username, date, gender, salary = employees_split
        info = {"id": id, "username": username, "date": date, "gender": gender, "salary": salary}
        data.append(info)

    return data


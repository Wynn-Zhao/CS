import csv
import dashboard

def main():
    check = [input("Enter Login User Name: "), input("Enter Login Password: ")]

    users = []
    with open('Users.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            users.append(row)

    login = True
    wrong_name = False
    wrong_password = False 

    for info in users:
        if info == check:
            login = True
            break
        else:
            login = False

    if login:
        print("Login succeed, welcome!")
        dashboard.main()
    else:
        for info in users:
            if info[0] == check[0]:
                wrong_name = False
            else:
                wrong_name = True
            if info[1] == check[1]:
                wrong_password = False
            else:
                wrong_password = True
        if wrong_name and wrong_password:
            print("Come on! Account doesn't exist at first place")
        elif wrong_name:
            print("Wrong user name, how dare you?")
        elif wrong_password:
            print("Wrong password, why don't you memerize it correctly?")

if __name__ == "__main__":
    main()



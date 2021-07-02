import csv
from csv import writer

def main():
    check = []
    name = input("Register User Name: ")

    with open('Users.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            check.append(row)

    for existing_name in check:
        while existing_name[0] == name:
            print('Existing User Name')
            name = input("Register User Name Again: ")

    password = input("Register Password: ")
    repassword = input("Re-enter Your Register Password: ")

    while password != repassword:
        print("Password doesn't match")
        password = input("Register Passord Again: ")
        repassword = input("Re-enter Your Register Password Again: ")

    data = [name, password]

    def register(data):
        with open('Users.csv', 'a+', newline='') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            csv_writer = writer(file) # Create a writer object from csv module
            csv_writer.writerow(data) # Add contents of list as last row in the csv file
        print("Register succeed, congratulations!")
    register(data)

if __name__ == '__main__':
    main()
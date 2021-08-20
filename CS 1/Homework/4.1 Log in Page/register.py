import csv
from csv import writer
import main

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
        print("Come on! Password doesn't match")
        password = input("Register Passord Again: ")
        repassword = input("Re-enter Your Register Password Again: ")

    data = [name, password]

    def register(data):
        with open('Users.csv', 'a+', newline='') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            csv_writer = writer(file) # Create a writer object from csv module
            csv_writer.writerow(data) # Add contents of list as last row in the csv file
        print("Register succeed, congratulations!")
        print('-------------')
    register(data)

    if input('Type "yes: if you want to start the program again: ') == 'yes':
        main.main()

if __name__ == '__main__':
    main()
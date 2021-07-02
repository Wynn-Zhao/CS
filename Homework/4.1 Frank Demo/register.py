import csv

def main():
    username=input('Please type in your username: ')
    password=input('Please type in your password: ')
    check=input('Please type in your password again:')
    while password!=check:
        print('Password does not match!!!')
        username=input('Please type in your username: ')
        password=input('Please type in your password: ')
        check=input('Please type in your password again: ')

    new=[username,password]
    data = []
    with open('Username.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            data.append(row)


    for name in data:
        while username==name[0]:
            print('Username Already Used')
            username=input('Please type in your username: ')
            password=input('Please type in your password: ')
            check=input('Please type in your password again: ')

    new=[username,password]
    data.append(new)

    with open('Username.csv', 'w',newline='') as file:
        csv_writer = csv.writer(file, delimiter = ',')
        for row in data:
            csv_writer.writerow(row)

if __name__ == '__main__':
    main()
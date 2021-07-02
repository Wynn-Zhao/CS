import csv
def user():
    username=input('Please type in your username ')
    return username
def word():
    password=input('Please type in your password ')
    return password
def main():
    username=user()
    password=word()
    new=[username,password]

    data = []
    with open('Username.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            data.append(row)

    hello=True
    for name in data:
        if name == new:
            hello=True
            break
        else:
            hello=False

    if hello:
        print('Login Successfully')
        name=[username]
        with open('login.csv', 'w',newline='') as file:
            csv_writer = csv.writer(file, delimiter = ',')
            csv_writer.writerow(name)
        return True
    else:
        print('Wrong Username or Password')
        return False

if __name__ == '__main__':
    main()

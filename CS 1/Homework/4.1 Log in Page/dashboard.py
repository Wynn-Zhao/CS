import csv
import main

def main():
    if input('Type "yes" if you want to check all users: ') == 'yes':
        data = []
        with open('Users.csv') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                data.append(row)
        for user in data:
            print(user[0])
    else:
        print("Alright")

    info = []
    no_such_user = True
    if input('Type "yes" if you want to change your password: ') == 'yes':
        with open('Users.csv') as file:
            csv_reader = csv.reader(file, delimiter = ',')
            for row in csv_reader:
                info.append(row)
        name = input('Re-enter your user name: ')
        for row in info:
            if row[0] == name:
                while input('Re-enter your password: ') != row[1]:
                    print("Password doesn't match!")
                no_such_user = False
                a = input('Enter your new password: ')
                b = input('Re-enter your new password: ')
                while a != b:
                    print("Password does't match! What's wrong with you?")
                    a = input('Enter your new password again: ')
                    b = input('Re-enter your new password again: ')
                row[1] = b
                with open('Users.csv', 'w', newline='') as file:
                    csv_writer = csv.writer(file, delimiter = ',')
                    for Row in info:
                        csv_writer.writerow(Row)
                print('Password changed successfully!') 
                print('Exiting system, good luck!')               
                break
    else:
        print('Okay, exiting system')
        no_such_user = False

        while no_such_user:
            print('Why would you enter your name wrong?')
            if input('Type "yes" if you still want to change your password: ') == 'yes':
                print("Don't make the sily mistake this time! I am busy!")
                name = input('Re-enter your user name again: ')
                no_such_user = True 
                for row in info:
                    if row[0] == name:
                        while input('Re-enter your password: ') != row[1]:
                            print("Password doesn't match!")
                            input('Re-enter your password: ')
                        no_such_user = False
                        a = input('Enter your new password again: ')
                        b = input('Re-enter your new password again: ')
                        while a != b:
                            print("Password does't match! What's wrong with you?")
                            a = input('Enter your new password again: ')
                            b = input('Re-enter your new password again: ')
                        row[1] = b
                        with open('Users.csv', 'w', newline='') as file:
                            csv_writer = csv.writer(file, delimiter = ',')
                            for Row in info:
                                csv_writer.writerow(Row)
                        print('Exiting system, good luck!')               
                        break
            else:
                print('Good luck')
                no_such_user = False


if __name__ == '__main__':
    main()
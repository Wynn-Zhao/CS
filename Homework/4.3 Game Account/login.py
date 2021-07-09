import csv
from csv import writer
import register

def main():
    check = [input("Enter Login User Name: "), input("Enter Login Password: ")]

    users = []
    with open('users.csv') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader:
            users.append(row)

    login = True
    index = 0
    wrong_name = False
    wrong_password = False 

    for info in users:
        if info[0] == check[0] and info[1] == check[1]:
            login = True
            print("-------------")
            print("Login succeed, welcome!")
            break
        else:
            login = False
            index += 1

    if login == False:
        for info in users:
            if info[0] == check[0]:
                wrong_name = False
                break
            else: 
                wrong_name = True
            if info[1] == check[1]:
                wrong_password = False
                break
            else:
                wrong_password = True
        if wrong_name:
            print("Come on! Account doesn't exist at first place")
            if input('Do you want to register? Type "yes" if you want: ') == 'yes':
                register.main()
                print('Exiting system')
            else:
                print('Sure, exiting system.')
        elif wrong_password:
            print("Wrong password, why don't you memerize it correctly?")
            print(":(")
            print("Exiting system, please re-start the proccess")

    # Money: check, deposit, and withdraw
    if login:
        if input('Type "yes" if you want to enter the financial system of your account: ') == 'yes':
            print("-------------")
            print('Welcome to the financial system!')
            if input('Type "yes" if you want to check the amount of money in your account: ') == 'yes':
                print("$" + str(users[index][2]))
                print('------------')
            else:
                print("Okay, hope you have it in your mind")
                print('------------')

            if input('Type "yes" if you want to deposit money in your account: ') == 'yes':
                amount_deposit = input('Enter the amount of money you want to deposit (please enter integer): ')
                while int(amount_deposit) < 0:
                    print('------------')
                    print("Why would you even think to deposit negative amount of money?")
                    amount_deposit = input('Enter the amount of money you want to deposit again (please enter integer): ')
                users[index][2] = int(users[index][2]) + int(amount_deposit)
                if int(amount_deposit) == 0:
                    print('Thank you for wasting my time, your account still have $' + str(users[index][2]))
                    print('------------')
                else:
                    print('Deposit succeed! You now have $' + str(users[index][2]) + ' in your account') 
                    print('------------')
            else:
                print('Sure, even though it makes me sad')
                print('------------')

            if input('Type "yes" if you want to withdraw money in your account: ') == 'yes':
                print('FYI, your account has $' + str(users[index][2]))
                amount_withdraw = input('Enter the amount of money you want to withdraw (please enter integer): ')
                while int(amount_withdraw) < 0:
                    print('-----------')
                    print("Tell me please, how to withdraw negative amount of money?")
                    amount_withdraw = input('Enter the amount of money you want to withdraw again (please enter integer): ')
                while int(users[index][2]) - int(amount_withdraw) < 0:
                    print('-----------')
                    print("You know this, your acccount doesn't have this much money to deposit")
                    amount_withdraw = input('Enter the amount of money you want to withdraw again (please enter integer): ')
                users[index][2] = int(users[index][2]) - int(amount_withdraw)
                if int(amount_withdraw) == 0:
                    print('-----------')
                    print('Thank you for wasting my time, your account still have $' + str(users[index][2]))
                else:
                    print('-----------')
                    print('Withdraw succeed! You now have $' + str(users[index][2]) + ' in your account')
            else:
                print('Great!')

        else:
            print('Understand')

    # Friend system
    if login:
        print('------------')
        if input('Type "yes" if you want to enter the friend system in your account: ') == 'yes':
            print("-------------")
            print('Welcome to the friend system!')
            print()
            loop = 0
            for i in users[index]:
                loop += 1
            if loop == 3:
                print('You have no friend yet')
            else:
                print('You are friends with: ' + str(users[index][3:])[1:-1])

            while input('Type "yes" if you want to add friend: ') == 'yes':
                new_friend = input("Enter the person you want to add as your friend: ")
                check_new = False
                check_exist = True
                for name in users[index][3:]:
                    if name == new_friend:
                        check_new = True
                        break
                for account in users:
                    if account[0] == new_friend:
                        check_exist = False
                        break
                while check_new or check_exist:
                    if check_new:
                        print('The account you entered is already your friend, please remember it!')
                    if check_exist:
                        print("-Really? The account name you entered doesn't exist!")
                        print('------------')
                        if input('Type "yes" if you want to check all existing users: ') == 'yes':
                            for account in users:
                                print(account[0])
                    new_friend = input("Enter the person you want to add as your friend again: ")
                    for name in users[index][3:]:
                        if name == new_friend:
                            check_new = True
                            break
                        else:
                            check_new = False
                    for account in users:
                        if account[0] == new_friend:
                            check_exist = False
                            break
                        else:
                            check_exist = True
                    
                users[index].append(new_friend) 
                if new_friend == users[index][0]:
                    print('Congratulations! You are now friends with yourself!')
                    print('------------')
                else:
                    print('Congratulations! You are now friends with ' + str(new_friend))
                    print('------------')

            # if input('Type "yes" if you want to check money of your friends') == 'yes':
        print('------------')
                




    with open('users.csv', 'w', newline='') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        csv_writer = writer(file) # Create a writer object from csv module
        for row in users:
            csv_writer.writerow(row) # Add contents of list as last row in the csv file

if __name__ == "__main__":
    main()



import csv
import register
import login
import dashboard

def main():
    print("Welcome to Wynn's database!")
    if input('Type "yes" if you want to register new account: ') == 'yes':
        print("Welcome to register page!")
        register.main()
    else:
        print('Alright')
    if input('Type "yes" if you want to login: ') == 'yes':
        print("Welcome to login page!")
        login.main()
    else:
        print('I see.')
        print("Exiting system, good luck!")


if __name__ == '__main__':
    main()
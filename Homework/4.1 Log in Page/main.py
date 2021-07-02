import csv
import register
import login
import dashboard

def main():
    print("Welcome to Wynn's database!")
    if input('Type "yes" if you want to register new account: ') == 'yes':
        print("Welcome to register page!")
        register.main()
    if input('Type "yes" if you want to login: '):
        print("Welcome to login page!")
        login.main()


if __name__ == '__main__':
    main()
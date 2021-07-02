import csv
import register
import login
import dashboard
def main():
    name='username'
    hello=input('Do you want to register: ')
    if hello=='yes':
        print('hello')
        register.main()
    hi=input('Do you want to login: ')
    if hi=='yes':
        if login.main():
            dashboard.main()
        

if __name__ == '__main__':
    main()
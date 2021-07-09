import register
import login
import main_bj

def main():
    if input('Type "yes" if you want to register: ') == 'yes':
        register.main()
        print('Welcome to login page!')
    else:
        print('-----------')
        print('Okay, you are now in the login page')

    if input('Type "yes" if you want to login: ') == 'yes':
        login.main()
        print('-----------')
    #     print('You are now at the gamming page')
    #     if input('Types "yes" if you want to play Black Jack: ') == 'yes':
    #         main_bj()
    #         print('Exiting system')
    # else:
    #     print('Alright, exiting system, good luck!')
    else:
        print('-----------')
        print('Alright, exiting system, good luck!')

if __name__ == '__main__':
    main()
import my_math

def my_input():
    num = int(input('your number: '))
    return num

def main():
    x = my_input()
    print('Fibo number: ', my_math.fibo(x))

if __name__ == '__main__':
    main()
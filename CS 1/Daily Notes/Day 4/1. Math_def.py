def fibo(n):
    if (n==1 or n==2):
        return 1
    return fibo(n-1)+fibo(n-2)


def is_prime(n):
    if (n==1):
        return False

    for i in range(2,int(n**0.5)+1):
        if (n%i==0):
            return False

    return True


def area(a,b,c):
    p = (a+b+c)*0.5
    return (p*(p-a)*(p-b)*(p-c))**0.5


def main():
    sides = input().split(',')

    x = list(map(lambda x: int(x), sides))
    
    print(area(x[0], x[1], x[2]))

if __name__ == '__main__':
    main()
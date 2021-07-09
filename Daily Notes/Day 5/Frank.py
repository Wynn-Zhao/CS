import sys
import math

def areac(r):
    return 3.14*r*r

def peremiterc(r):
    return 2*r*3.14

def peremitert(a,b,c):
    return a+b+c

def area_triangle(a,b,c):
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

def peremiterr(a,b):
    return a+b+c+d

def arear(a,b):
    return a*b


def main():
    # python calc.py add 2 10 6 9 12 20
    function = sys.argv[1]
    specify = sys.argv[2]
    str_nums = sys.argv[3:]

    nums = list(map(int, str_nums))
    
    if (function=='rectangle' and specify=='area'):
        return arear(nums[0], nums[1])
    if (function == 'rectangle' and specify=='peremiter'):
        return peremiterr(nums[0], nums[1])
    if (function == 'circle' and specify=='area'):
        return areac(nums[0])
    if (function == 'circle' and specify=='peremiter'):
        return peremiterc(nums[0])
    if (function == 'triangle' and specify=='area'):
        return area_triangle(nums[0], nums[1], nums[2])
    if (function == 'triangle' and specify=='peremiter'):
        return peremitert(nums[0], nums[1], nums[2])


if __name__ == '__main__':
    print(main())
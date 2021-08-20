import sys
import math

def area_triangle(a, b, c):
    s = (a + b + c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5

def perimeter_triangle(a,b,c):
    return a + b + c

def area_circle(r):
    return 3.14*(r*r)

def perimeter_circle(r):
    return 3.14*(2*r)

def area_rec(a, b):
    return a*b

def perimeter_rec(a,b):
    return 2*(a + b)


def main():
    function_1 = sys.argv[1]
    function_2 = sys.argv[2]
    str_nums = sys.argv[3:]

    nums = list(map(int, str_nums))

    if (function_1 == 'area' and function_2 == 'triangle'):
        return area_triangle(nums[0], nums[1], nums[2])

    if (function_1 == 'area' and function_2 == 'circle'):
        return area_circle(nums[0])

    if (function_1 == 'area' and function_2 == 'rectangle'):
        return area_rec(nums[0], nums[1])

    if (function_1 == 'perimeter' and function_2 == 'triangle'):
        return perimeter_triangle(nums[0], nums[1], nums[2])

    if (function_1 == 'perimeter' and function_2 == 'circle'):
        return perimeter_circle(nums[0])

    if (function_1 == 'perimeter' and function_2 == 'rectangle'):
        return perimeter_rec(nums[0], nums[1])

if __name__ == '__main__':
    print(main())
from math import *
#Последовательность треугольных чисел образуется путем сложения натуральных чисел. К примеру, 7-ое треугольное число равно 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. Первые десять треугольных чисел:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#Перечислим делители первых семи треугольных чисел:

# 1: 1
#3: 1, 3
# 6: 1, 2, 3, 6
#10: 1, 2, 5, 10
#15: 1, 3, 5, 15
#21: 1, 3, 7, 21
#28: 1, 2, 4, 7, 14, 28
#Как мы видим, 28 - первое треугольное число, у которого более пяти делителей.

#Каково первое треугольное число, у которого более пятисот делителей?

####

def get_triangle_number(x):
    number = 0
    if x > 0:
        for i in range(1, x+1):
            number += i
        return number


def gen_triangles():
    n = 1
    t = n
    while True:
        yield t
        n += 1
        t += n

triangles = gen_triangles()

def is_perf_sq(n):
    x=ceil((sqrt(n)))
    if x*x==n:
        return True
    else:
        return False

def count_factors(x):
    count = 2
    for i in range(2, ceil(sqrt(x))):
        if x % i == 0:
            count+=2
    if is_perf_sq(x):
        return count + 1
    else:
        return count

while True:
    number = next(triangles)
    count = count_factors(number)
    if count > 500:
        print('result:', number)
        break
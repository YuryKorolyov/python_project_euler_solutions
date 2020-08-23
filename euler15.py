#Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться только вниз или вправо, существует ровно 6 маршрутов до правого нижнего угла сетки.


#Сколько существует таких маршрутов в сетке 20×20?


# Треугольник Паскаля, биноминальный коэффициент

from math import *

def binominal_coef(a, b):
    c = a + b
    coef = factorial(c)
    coef/= factorial(a)*factorial(b)
    return int(coef)

def routes(n):
    result = 1

    for i in range(1, n+1):
        result = result * (i + n) / i
    return result

print(routes(20)) # 137846528820


# Рекурсивный алгоритм

def count_routes1(m, n):
    if n == 0 or m == 0:
        return 1
    else:
        return count_routes(m-1, n) + count_routes(m, n - 1)


# Оптимизированный рекурсивный алгоритм

cache = {}

def count_routes2(m, n):
    print(cache)
    if n == 0 or m == 0:
        return 1
    elif (m, n) in cache:
        return cache[m, n]
    else:
        cache[m, n] = count_routes2(m - 1, n) + count_routes2(m, n - 1)
        return cache[m, n]
#print(count_routes2(1,1))



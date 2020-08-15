#Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

#Найдите сумму всех простых чисел меньше двух миллионов.

# Находим все простые числа меньше двух миллионов.

import math

def eratoshenes(number):
    sieve = list(range(number))
    sieve[1] = 0
    for i in sieve:
        if sieve[i] > 1:
            for b in range(i+i, len(sieve), i):
               sieve[b] = 0
    return sieve

def sum_of_primes(number):
    sum = 0
    for i in eratoshenes(number):
        sum+=i
    return sum

print(sum_of_primes(2000000))
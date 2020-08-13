#Простые делители числа 13195 - это 5, 7, 13 и 29.

#Каков самый большой делитель числа 600851475143, являющийся простым числом?
import math
number = 600851475143

# Получаем делители числа

def get_factors(number):
    factors = []
    for i in range(1, int(math.sqrt(number))+1):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)
    return factors

print(get_factors(10))

# Определяем, является ли делитель простым числом

def is_prime(number):
    if len(get_factors(number)) == 2 :
        return True
    else:
        return False

print(is_prime(1))

# Находим наибольший простой делитель

all_factors = get_factors(number)
print(all_factors)
largest_prime_factor = 0

for factor in all_factors:
   if is_prime(factor) and factor > largest_prime_factor:
       largest_prime_factor = factor

print(largest_prime_factor)

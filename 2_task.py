# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.



def fib_number(number):
    fib1 = 0
    fib2 = 1
    if number == 1:
        return fib1
    elif number == 2:
        return fib2
    else:
        for i in range(number):
            fn = fib1 + fib2
            fib1, fib2 = fib2, fn
        return fn

print(fib_number())

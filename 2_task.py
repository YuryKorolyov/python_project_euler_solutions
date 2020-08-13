# Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.



def fib_number(number):
    fib0 = 0
    fib1 = 1
    fib2 = 2
    if number == 0:
        return fib0
    elif number == fib1:
        return fib1
    elif number == fib2:
        return fib2
    else:
        for i in range(number):
            fn = fib0 + fib1
            fib0, fib1 = fib1, fn
        return fn

def sum_of_fib_numbers(x):
    sum = 0
    fn = 0
    i = 1
    while fn < x:
        fn = fib_number(i)
        if fn < x:
            i+=1
        else:
            break
        if fn % 2 == 0:
            sum+=fn
    return sum

print(sum_of_fib_numbers(4000000)) # 4613732

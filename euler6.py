#Сумма квадратов первых десяти натуральных чисел равна

#1**2 + 2**2 + ... + 10**2 = 385
# суммы первых десяти натуральных чисел равен

#(1 + 2 + ... + 10)**2 = 552 = 3025
#Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.

#Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.

def sum_of_squares(range_end):
    s = 0
    for i in range(range_end):
        s+=i**2
    return s
print(sum_of_squares(100))
def square_of_sum(range_end):
    s = 0
    for i in range(range_end):
        s+=i
    s = s**2
    return s
print(square_of_sum(100))
def difference():
    dif = square_of_sum(101) - sum_of_squares(101)
    return dif

print(difference())


input()

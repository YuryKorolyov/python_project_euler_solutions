#Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

#Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.

string = 'test'

print(string[::-1])

def is_palindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False

max = 0
for i in range(100, 1000):
    for x in range(100, 1000):
        c = i * x
        if is_palindrome(c) and c > max:
             max = c
print(max)

input()

    


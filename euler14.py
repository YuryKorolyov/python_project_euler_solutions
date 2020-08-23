#Следующая повторяющаяся последовательность определена для множества натуральных чисел:

#n → n/2 (n - четное)
#n → 3n + 1 (n - нечетное)

#Используя описанное выше правило и начиная с 13, сгенерируется следующая последовательность:

#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#Получившаяся последовательность (начиная с 13 и заканчивая 1) содержит 10 элементов. Хотя это до сих пор и не доказано (проблема Коллатца (Collatz)), предполагается, что все сгенерированные таким образом последовательности оканчиваются на 1.

#Какой начальный элемент меньше миллиона генерирует самую длинную последовательность?

#Примечание: Следующие за первым элементы последовательности могут быть больше миллиона.

def gen_sequence(number):
    sequence = []
    count = 0
    n = number
    while n > 1:
        if n == 2:
            count+= 2
            #sequence.append(int(n/2))
            break
        elif n % 2 == 0:
            count+=1
            #sequence.append(int(n))
            n = n / 2
        else:
            count += 1
            n = 3 *n + 1
    return count
print(gen_sequence(12))

biggest = 0
for i in range(0, 1000000):
    c = gen_sequence(i)
    if c > biggest:
        biggest = c 
        print(biggest, i)

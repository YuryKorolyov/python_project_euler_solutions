#Если записать числа от 1 до 5 английскими словами (one, two, three, four, five), то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.

#Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?


#Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) состоит из 23 букв,
#число 115 (one hundred and fifteen) - из 20 букв. 
#Использование "and" при записи чисел соответствует правилам британского английского.

#from math import *

data1 = {
    0:0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 
    10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,
    20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6,
    100:7,
    1000:8
}

def number_digits(x):
    digits = []
    for i in range(0, len(str(x))):
        digits.append(int(str(x)[i]))
    for i in range(0, len(digits)):
        digits[i] *= 10**len(digits[i:-1])
    if digits[0] >= 100 and digits[0]< 1000:
        digits.insert(0, int(digits[0]/100))
        digits[1] = int(digits[1] / digits[0])
    elif digits[0] >=1000:
        digits.insert(0, int(digits[0]/1000))
        digits[1] = int(digits[1]/digits[0])
        print(digits[0])
    return digits
print(number_digits(711))

sum = 0

for i in range(1, 1001):
    if i > 100 and i % 100 !=0:
        sum+=3
    digits = number_digits(i)
    if len(digits) >=2 and digits[-2] + digits[-1] <=20:
        digits[-2] = digits[-2] + digits[-1]
        del digits[-1]
    print(digits)
    for c in digits:
        sum+=data1[c]
print(sum)
# answer - 21124


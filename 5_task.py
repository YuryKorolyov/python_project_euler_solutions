#2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

#Какое самое маленькое число делится нацело на все числа от 1 до 20?

list = [i for i in range(1, 21)]
print(list)

#def find_smallest(list):
    #if len(list) == 2:
        #c = list[0] * list[1]
        #return c
   # else:
       # z = list[-1] * find_smallest(list[:-1])
       # a = 0
        #while a < z:
         #   a+=list[-1]
          #  for i in range(1, list[-1]+1):
           #     if a % i == 0:
            #        s = a
         
                
def isDivisibleTo20(number):
    for i in range(1, 21):
        if number % i !=0:
            return False
    return True

number = 20

while True:
    if isDivisibleTo20(number):
        break
    else:
        number += 20
print(number)
#print(find_smallest(list))

input()
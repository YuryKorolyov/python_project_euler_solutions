#Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

#a2 + b2 = c2
#Например, 32 + 42 = 9 + 16 = 25 = 52.

#Существует только одна тройка Пифагора, для которой a + b + c = 1000.
#Найдите произведение abc.



def find_Pythagorean_triplet_reproduction(sum):

    for a in range(1, sum - 1):
      for b in range(1, sum - 1):
          c = sum -(a + b)
          if a**2 + b**2 == c**2:
              return (a*b*c)

print(find_Pythagorean_triplet_reproduction(1000)) # 31875000
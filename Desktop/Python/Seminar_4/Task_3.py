# Задайте два числа. Напишите программу, которая найдёт НОК 
# (наименьшее общее кратное) этих двух чисел.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if b > a:
    a, b = b, a
for i in range(1, b):
    if (a * (i)) % a == 0 and (a * (i)) % b == 0:
        print(i)
        break
print(f'{a} {i} = {a * (i)}')
print(f'{a} {i} = {a * (i)}')
print(f'{a} {i} = {a * (i)}')
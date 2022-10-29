# Реализуйте алгоритм перемешивания списка.

import random

list = [2, 5, 3, 6, 12]
print('Исходный вариант списка: ' + str(list))

for i in range(len(list)-1, 0, -1):
    j = random.randint(0, i + 1)
    list [i], list [j] = list [j], list [i]
print('Перемешанный вариант списка: ' + str(list))
     
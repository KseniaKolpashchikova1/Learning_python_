# 1.Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

daynumber = int(input ('Введите номер дня недели: '))
if (daynumber > 5) and (daynumber <=7):
    print('День недели является выходным')
elif (daynumber > 1) and (daynumber <=5):
    print('День недели является будним') 
else:
    print('Такого дня недели не существует! Проверьте корректность введенного значения') 

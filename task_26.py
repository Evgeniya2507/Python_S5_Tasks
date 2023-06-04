# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B 
# с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

a = int(input('Введите целое число: '))
b = int(input('Введите степень этого числа: '))
def Extent_a(a, b):
    if b == 0:
        return 1
    if b % 2 == 0:
        return Extent_a(a, b//2) * Extent_a(a, b//2)
    else:
        return Extent_a(a, b - 1) * a

print(Extent_a(a, b))
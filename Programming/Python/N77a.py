﻿# Дано натуральное число n. Вычислить: 2^n

print("Введите любое целое число")
n = float(input("Число: "))
while n < 0 or n - int(n) != 0:
    print("Число должно быть целым строго больше нуля.")
    n = float(input("Число: "))
n = int(n)

n = 2 ** n

print("Число: ", n)

input('Нажмите ENTER для выхода') 
﻿# Даны натуральное n, действительное х. Вычислить: sinх + sin^2 х + ... + sin^n х;

import math

print("Введите любое число")
x = float(input("Число: "))

print("Введите целое число больше нуля")
n = float(input("Натуральное число: "))
while n <= 0 or n - int(n) != 0:
    print("Число должно быть целым и больше нуля")
    n = float(input("Число: "))
n = int(n)

task = 1

for i in range(n):
    task = task * math.sin(x)

print(task)

input('Нажмите ENTER для выхода') 
# Даны натурально число n, действительное число x. Вычислить:

import math


print("Введите любое число")
x = float(input("Число: "))

print("Введите целое число больше нуля")
n = float(input("Натуральное число: "))
while n <= 0 or n - int(n) != 0:
    print("Число должно быть целым и больше нуля")
    n = float(input("Число: "))
n = int(n)

task = 0
i = 1

for t in range(n):
    task = task + ((x + math.cos(i * x)) / 2 ** i)

print("Ряд равен : ", task)

input('Нажмите ENTER для выхода') 
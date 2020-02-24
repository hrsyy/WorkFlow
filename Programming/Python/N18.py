# Треугольник задан величинами своих углов и радиусом описанной окружности. Найти стороны треугольника.

import math

print("Введите радиус окружности")
R = float(input("R= "))
while R <= 0:
    print("Число должно быть строго больше нуля.")
    R = float(input("R= "))

print("Введите углы A,B и C в градусах")
A = float(input("A= "))
B = float(input("B= "))
if A < 0 or B < 0:
    if A < 0:
        while A < 0:
            print("Число должно быть больше либо равно нулю.")
            A = float(input("A= "))
    if B < 0:
        while B < 0:
            print("Число должно быть больше либо равно нулю.")
            B = float(input("B= "))

C = 180 - A - B

a = 2 * R * (math.sin(A * ((math.pi) / 180)))
b = 2 * R * (math.sin(B * ((math.pi) / 180)))
c = 2 * R * (math.sin(C * ((math.pi) / 180)))

print("Сторона а = ", a)
print("Сторона b = ", b)
print("Сторона c = ", c)

input('Нажмите ENTER для выхода') 
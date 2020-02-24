#Даны x, y, z. Вычислить a, b, если:

import math

print("Введите любые числа")
z = float(input("z= "))
y = float(input("y= "))
x = float(input("x= "))

a = (math.sqrt(abs(x - 1)) - math.pow(abs(y), 1/3))/(1 + ((x ** 2) / 2) + ((y ** 2) / 4)) 
b = x * (math.atan(z) + math.exp(- x - 3))

print("a= ", a)
print("b= ", b)

input('Нажмите ENTER для выхода') 
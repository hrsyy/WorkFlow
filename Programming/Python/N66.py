# Даны целые числа k, m, действительные числа x, y, z. 
# При k < m^2, k = m^2, k > m^2 заменить модулем соответственно значения x, y или z, а два других значения уменьшить на 0,5.

import math
print("Введите целые числа")
k = float(input("k = "))
m = float(input("m = "))

while k <= 0 or k - int(k) != 0:
    print("Число должно быть целым и строго больше нуля")
    k = float(input("k = "))
while m <= 0 or m - int(m) != 0:
    print("Число должно быть целым и строго больше нуля")
    m = float(input("m = "))

k = int(k)
m = int(m)

print("Введите любые числа")
x = float(input("x = "))
y = float(input("y = "))
z = float(input("z = "))

if k < m ** 2 or k == m ** 2 or k > m **2:
    x = math.fabs(x)
    y -= 0.5
    z -= 0.5

print('x = ', x)
print('y = ', y)
print('z = ', z)

input('Нажмите ENTER для выхода') 
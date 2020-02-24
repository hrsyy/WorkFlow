# Если сумма трех попарно различных действительных чисел x, y, z меньше единицы,
# то наименьшее из этих трех чисел заменить полусуммой двух других;
# в противном случае заменить меньшее из x и y полусуммой двух оставшихся значений.

print("Введите 3 различающихся действительных числа")
x = (float(input("x = ")))
y = (float(input("y = ")))
z = (float(input("z = ")))

average = 0

L = [x, y, z]
a = min(L)
b = max(L)

L1 = [x, y]
c = min(L1)
d = max(L1)

if y < x < z or z < x < y:
    average = average + x
elif x < y < z or z < y < x:
    average = average + y
else:
   average = average + z

S = sum(L)
if S < 1:
    a = ((b + average) / 2)
    print("a = ", a)
else:
    c = ((d + average) / 2)
    print("c = ", c)

input('Нажмите ENTER для выхода') 

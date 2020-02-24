# Даны действительные числа a, b, c, d. Если a ≤ b ≤ c ≤ d, то каждое число заменить наибольшим из них; 
# если a > b > c > d, то числа оставить без изменения; в противном случае все числа заменяются их квадратами.

print("Введите действительные числа: ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))

L = [a, b, c, d]
m = max(L)

if a <= b <= c <= d:
    for i in L:
        for i in range(0, 3):
            L[i] = m
    print("Список: ", L)
elif a > b > c > d:
    print("Список: ", L)
else:
    L = [i*i for i in L]       
    print(L)

input('Нажмите ENTER для выхода') 
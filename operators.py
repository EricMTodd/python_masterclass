a = 12
b = 3

print(a + b)  # 15
print(a - b)  # 9
print(a * b)  # 36
print(a / b)  # 4.0
print(a // b)  # 4 Integer division is rounded down towards minus infinity
print(a % b)  # 0 Modulo: The remainder after integer division

print()

for i in range(1, a // b):
    print(i)

bun_price = 2.40
money = 15

print(money // bun_price)

print()

print(a + b / 3 - 4 * 12)  # -35.0
print(a + (b / 3) - (4 * 12))  # -35.0
print((((a + b) / 3) - 4) * 12)  # 12
print(((a + b) / 3 - 4) * 12)  # 12

c = a + b
d = c / 3
e = d - 4
print(e * 12)  # 12

print()

print(a / (b * a) / b)  # 0.1111111111111111

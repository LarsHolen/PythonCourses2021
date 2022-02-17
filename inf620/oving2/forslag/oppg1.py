#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
INF620, Øving 2, oppgave 1
@author: Knut Anders Stokke
'''

# 1.a
print(9 - 3)  # 6
print(8 * 2.5)  # 20.0
print(9 / 2)  # 4.5
print(9 / -2)  # -4.5
print(9 // -2)  # -5
print(9 % 2)  # 1
print(9.0 % 2)  # 1.0
print(9 % -2)  # -1
print(-9 % 2)  # 1
print(9 / -2.0)  # -4.5
print(4 + 3 * 5)  # 19
print((4 + 3) * 5)  # 35
print(abs(5 - 10))  # 5

# 1.b
print(3 ** 6)
print(4 * 2 + 3)
print((4 + 2) * 3)
print(100 // 6)
print(100 % 6)
print(100 / 6)

# 1.c
y = int(input("Skriv et årstall: "))
a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32

print("Første påskedag faller på dag " + str(p) + " av måneden " + str(n) + ".")

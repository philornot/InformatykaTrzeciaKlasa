from main import dane
from math import sqrt

l = dane()
ilekw, pw = 0, 0
for i in range(2000):
    if sqrt(l[i]) % 1 == 0:
        ilekw += 1
        if pw == 0:
            pw = l[i]

print(ilekw, pw)
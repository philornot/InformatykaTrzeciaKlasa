from main import dane1, dane2
l1 = dane1()
l2 = dane2()
wyn = 0

for i in range(1000):
    a = l1[i][-2] + l1[i][-1]
    b = l2[i][-2] + l2[i][-1]
    if a == b:
        wyn += 1

print(wyn)
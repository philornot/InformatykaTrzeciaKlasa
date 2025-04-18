from main import dane
l = dane()

wyn = 0

for i in range(199):
    if l[i] != l[i + 1][::-1]:
        wyn += 1

print(wyn)
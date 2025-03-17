from main import dane

l = dane()
wyn = 0

for i in range(len(l)):
    if l[i][-1:] == "4" and "0" not in l[i]:
        wyn += 1

print(wyn)
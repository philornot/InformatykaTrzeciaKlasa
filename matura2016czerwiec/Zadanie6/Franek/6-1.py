from main import dane

l = dane()
wyn = 0

for i in range(len(l)):
    if l[i][-1:] == "8":
        wyn += 1

print(wyn)
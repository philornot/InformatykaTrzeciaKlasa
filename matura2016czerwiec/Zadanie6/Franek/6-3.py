from main import dane

l = dane()
wyn = 0

for i in range(len(l)):
    if l[i][-1:] == "2":
        if int(l[i][:-1],2) % 2 == 0:
            wyn += 1

print(wyn)
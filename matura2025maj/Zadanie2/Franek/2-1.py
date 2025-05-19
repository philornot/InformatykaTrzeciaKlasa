l = list(open("../../dane2025maj/symbole.txt", "r"))
for i in range(len(l)):
    l[i] = l[i].strip()

wyn = 0
for i in range(len(l)):
    if l[i] == l[i][::-1]:
        wyn += 1

print(wyn)
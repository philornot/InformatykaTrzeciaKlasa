from main import dane, czy_p_3

l = dane()
wyn = 0
for i in range(500):
    if czy_p_3(int(l[i])) == "Tak":
        wyn += 1

print(wyn)
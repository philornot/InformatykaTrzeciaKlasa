from main import dane, sum_sil

l, wyn = dane(), []

for i in range(500):
    if sum_sil(l[i]) == int(l[i]):
        wyn.append(int(l[i]))

print(wyn)
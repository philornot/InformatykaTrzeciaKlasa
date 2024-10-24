from main import ile_bloków, lista_danych
L = lista_danych()

wyn = 0
for i in range(len(L)):
    if ile_bloków(L[i]) <= 2:
        wyn += 1

print(wyn)
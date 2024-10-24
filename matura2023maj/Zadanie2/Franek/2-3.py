from main import lista_danych
L, wyn = lista_danych(), []

for i in range(len(L)):
    wyn.append(int(L[i],2))

print(bin(max(wyn))[2::])
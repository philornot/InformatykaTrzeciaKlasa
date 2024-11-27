from main import lista, czy_pol
l, lwyn = lista(), []

for i in range(len(l)):
    if czy_pol(l[i]) == True:
        lwyn.append(l[i])

print(lwyn)
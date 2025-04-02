liczba = int(input("Wprowadź liczbę: "))
lista_cyfr = []
while liczba > 0:
    reszta = liczba % 10
    lista_cyfr.append(reszta)
    liczba = liczba // 10

print(f'\nCyfry: {lista_cyfr[::-1]}')
for cyfra in lista_cyfr[::-1]:
    print(cyfra)

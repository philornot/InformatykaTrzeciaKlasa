liczba = int(input("Wprowadź liczbę: "))
lista_cyfr = []
while liczba > 0:
    reszta = liczba % 10
    lista_cyfr.append(reszta)
    liczba = liczba // 10

print(f'\nCyfry: {lista_cyfr[::-1]}')
for cyfra in lista_cyfr[::-1]:
    print(cyfra)

# lub krócej:
# liczba = int(input("Wprowadź liczbę: "))
# lista_cyfr2 = []
# while liczba > 0:
#     lista_cyfr2.append( liczba % 10)
#     liczba = liczba // 10
# print(lista_cyfr2[::-1])
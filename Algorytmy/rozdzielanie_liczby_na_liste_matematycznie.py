liczba = 521
lista = []
while liczba >  0:
    modulo = liczba % 10
    lista.append(modulo)
    liczba = liczba // 10

lista_rev = lista[::-1]
print(lista_rev)

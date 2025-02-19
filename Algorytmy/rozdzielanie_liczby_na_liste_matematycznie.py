liczba = 521
lista = []
while liczba >  0:
    modulo = liczba % 10
    lista.append(modulo)
    liczba = liczba // 10

# żeby odwrócić listę można użyć [::-1]
lista_rev = lista[::-1]
print(lista_rev)

# bez odwracania (działamy na nie nieodwróconej liście)
n = len(lista)
liczba = 0
for i in range(n):
    liczba = liczba + lista[i] * 10 ** i

print(liczba)

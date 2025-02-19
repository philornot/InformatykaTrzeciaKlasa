from interfejs import czytaj_plik

liczby = czytaj_plik(czy_przyklad=False)

def silnia(liczba_int):
    if liczba_int == 0:
        return 1

    obliczona_silnia = 1
    n = liczba_int

    while n > 0:
        obliczona_silnia *= n
        n -= 1

    return obliczona_silnia

for liczba in liczby:
    silnie = []
    liczba_str = str(liczba)
    for cyfra in liczba_str:
        silnie.append(silnia(int(cyfra)))
    if sum(silnie) == liczba:
        print(liczba)


def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


plik = open('../../dane2025maj/dron.txt', 'r')
linie = plik.readlines()
plik.close()

licznik = 0

for linia in linie:
    liczby = linia.strip().split()
    a = int(liczby[0])
    b = int(liczby[1])

    a_bezwzgl = abs(a)
    b_bezwzgl = abs(b)

    if b_bezwzgl == 0:
        wspolny_dzielnik = a_bezwzgl
    else:
        wspolny_dzielnik = nwd(a_bezwzgl, b_bezwzgl)

    if wspolny_dzielnik > 1:
        licznik += 1

print(licznik)

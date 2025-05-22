plik = open('../../dane2025maj/dron.txt', 'r')
linie = plik.readlines()
plik.close()

punkty = []
x = 0
y = 0

for linia in linie:
    liczby = linia.strip().split()
    dx = int(liczby[0])
    dy = int(liczby[1])

    x += dx
    y += dy
    punkty.append((x, y))

licznik_w_kwadracie = 0
for punkt in punkty:
    px, py = punkt
    if 0 < px < 5000 and 0 < py < 5000:
        licznik_w_kwadracie += 1

print(licznik_w_kwadracie)

trojka_punktow = []
for i in range(len(punkty)):
    for j in range(len(punkty)):
        for k in range(len(punkty)):
            if i != j and j != k and i != k:
                x1, y1 = punkty[i]
                x2, y2 = punkty[j]
                x3, y3 = punkty[k]

                srodek_x = (x1 + x3) / 2
                srodek_y = (y1 + y3) / 2

                if x2 == srodek_x and y2 == srodek_y:
                    trojka = [punkty[i], punkty[j], punkty[k]]
                    trojka.sort()
                    if trojka not in trojka_punktow:
                        trojka_punktow.append(trojka)

if trojka_punktow:
    wynik = trojka_punktow[0]
    print(f"({wynik[0][0]}, {wynik[0][1]}), ({wynik[1][0]}, {wynik[1][1]}), ({wynik[2][0]}, {wynik[2][1]})")

from interfejs import odczytaj_tabele

# w bit18.txt jest <km autostrady> <prędkość ciężarówek>
#  jeśli szybszy pojazd napotka wolniejszy, to zwalnia i dostosowuje prędkość do auta wolniejszego
# czyli jeśli na następnym km jest mniejsza v, tworzy się kolumna

# Wczytujemy dane
autostrada = odczytaj_tabele(czy_przyklad=True)

# Inicjalizujemy licznik kolumn
liczba_kolumn = 0

# Znajdź pierwszy i ostatni kilometr
pierwszy_km = list(autostrada.keys())[0]
ostatni_km = list(autostrada.keys())[-1]

# Przechodzimy po wszystkich kilometrach (oprócz ostatniego)
for km in range(pierwszy_km, ostatni_km):
    # Sprawdzamy czy mamy pomiar dla tego kilometra i następnego
    if km in autostrada and km + 1 in autostrada:
        # Jeśli prędkość na następnym kilometrze jest mniejsza, mamy kolumnę
        if autostrada[km] > autostrada[km + 1]:
            liczba_kolumn += 1

print(liczba_kolumn)
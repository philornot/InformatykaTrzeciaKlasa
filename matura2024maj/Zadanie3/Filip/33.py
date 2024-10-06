from interfejs import nieparz_skrot_plik


# Funkcja obliczająca NWD bez użycia zewnętrznych bibliotek
def nwd(a, b):
    while b != 0:
        a, b = b, a % b  # obliczamy resztę z dzielenia aż b stanie się zerem
    return a  # zwracamy największy wspólny dzielnik (a)


# Ścieżka do pliku z danymi
plik = "../../../matura2024maj/dane2024maj/skrot2.txt"

# Oblicz nieparzyste skróty dla liczb w pliku
np = nieparz_skrot_plik(plik)

# Lista na liczby, które spełniają warunek (NWD = 7)
wynik = []

# Przejdź przez każdą liczbę i jej skrót, obliczając NWD
for liczba, skrot in np.items():
    if skrot is not None:  # sprawdzamy, czy skrót istnieje
        wynik_nwd = nwd(liczba, skrot)  # obliczamy NWD używając naszej funkcji
        if wynik_nwd == 7:  # sprawdzamy, czy NWD wynosi 7
            wynik.append(liczba)  # jeśli tak, dodajemy liczbę do listy wyników

# Zapisz wynik do pliku wynik3_3.txt
with open("wyniki3_3.txt", "w") as f:
    for liczba in wynik:
        f.write(f"{liczba}\n")

print(f"Wynik zapisano do pliku 'wyniki3_3.txt'.")

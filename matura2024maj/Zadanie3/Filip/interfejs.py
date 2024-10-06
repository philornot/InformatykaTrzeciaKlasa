# Funkcja obliczająca nieparzysty skrót liczby n
def nieparz_skrot(n):
    m_list = []  # lista do przechowywania cyfr, które są nieparzyste
    n = n.strip()  # usuń białe znaki z początku i końca tekstu

    # Iteruj przez każdą cyfrę w liczbie
    for char in str(n):
        if int(char) % 2 == 1:  # Sprawdź, czy cyfra jest nieparzysta
            m_list.append(char)  # Jeśli tak, dodaj ją do listy

    m = ''.join(m_list)  # Złącz cyfry w jedną liczbę
    if m == '':  # Jeśli lista jest pusta (nie było nieparzystych cyfr)
        return None  # Zwróć None (brak nieparzystego skrótu)
    else:
        m = int(m)  # Konwertuj wynik z powrotem na liczbę
    return m  # Zwróć nieparzysty skrót


# Funkcja obliczająca nieparzyste skróty dla wszystkich liczb w pliku
def nieparz_skrot_plik(plik):
    # Otwórz plik i wczytaj jego linie
    with open(plik, encoding="utf-8") as f:
        lines = f.readlines()  # wczytaj wszystkie linie pliku

    np = {}  # słownik do przechowywania liczb i ich skrótów

    # Iteruj przez każdą linię w pliku
    for i in lines:
        np[int(i.strip())] = nieparz_skrot(i)  # Przypisz skrót liczby do słownika

    return np  # Zwróć słownik liczb i ich nieparzystych skrótów

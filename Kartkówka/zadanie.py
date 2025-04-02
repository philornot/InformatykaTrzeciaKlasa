def rozbij():
    liczba = input("Podaj liczbę: ")
    n, a, liczba = len(liczba), 10 ** (len(liczba) - 1), int(liczba)
    for i in range(n):
        print(int(liczba // a))
        liczba, a  = liczba % a, a/10

rozbij()
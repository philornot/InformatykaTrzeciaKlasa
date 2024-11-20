from interfejs import zamien_na_bin

licznik = 0  # tylko dla względów kosmetycznych :)
while True:
    if licznik == 0:
        liczba_10 = input("Wprowadź liczbę dziesiętną: ")
    else:
        liczba_10 = input("\nWprowadź liczbę dziesiętną: ")

    if liczba_10 == "":
        print("Zakończono")
        break

    print(zamien_na_bin(int(liczba_10)))
    licznik = licznik + 1

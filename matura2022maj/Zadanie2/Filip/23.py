from interfejs import wynik_algorytmu


def wprowadz_slowo():
    print("Wprowadź słowo (ENTER żeby skończyć):")
    slowo = ''
    while True:
        litera = input("\nlitera: ")
        if litera == "":
            break
        m = int(input("m: "))

        slowo += litera * m

    print('\n========\n')
    return slowo


wynik_algorytmu(wprowadz_slowo())  # 990 :)

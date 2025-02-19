from interfejs import odczytaj_wymiary

# todo zamień kolejnosc arg pls :)
def czy_prostokat_sie_miesci(szerokosc1, wysokosc1, szerokosc2, wysokosc2):
    if szerokosc1 <= szerokosc2 and wysokosc1 <= wysokosc2:
        return True
    else:
        return False

wysokosc_tabela, szerokosc_tabela = odczytaj_wymiary(czy_przyklad=False)
for i in wysokosc_tabela, szerokosc_tabela:
    if czy_prostokat_sie_miesci()
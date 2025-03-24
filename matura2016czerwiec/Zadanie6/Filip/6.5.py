from interfejs import czytaj_plik

def na_dzies(num, system='2'):
    decimal_value = 0
    base = 1
    while (num):
        last_digit = num % 10
        num = num // 10
        decimal_value += last_digit * base
        base = base * int(system)
    # print("The decimal value is :",decimal_value)
    return decimal_value

dane = czytaj_plik()
dzies_maks = 0
zakodowana_maks = 0
dzies_min = 2137731221377312
zakodowana_min = 0

for liczba in dane:
    if na_dzies(int(liczba[:-1]), liczba[-1]) > dzies_maks:
        dzies_maks = na_dzies(int(liczba[:-1]), liczba[-1])
        zakodowana_maks = liczba
    if na_dzies(int(liczba[:-1]), liczba[-1]) < dzies_min:
        dzies_min = na_dzies(int(liczba[:-1]), liczba[-1])
        zakodowana_min = liczba

print(zakodowana_maks, dzies_maks)
print(zakodowana_min, dzies_min)
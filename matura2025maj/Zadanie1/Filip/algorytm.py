liczba_wyw = 0

def przestaw(n):
    global liczba_wyw
    liczba_wyw += 1
    r = n % 100
    a = r // 10
    b = r % 10
    n = n // 100
    if n > 0:
        w_temp, liczba_wyw_temp = przestaw(n)
        w = a + 10 * b + 100 * w_temp
    else:
        if a > 0:
            w = a + 10 * b
        else:
            w = b
    return w, liczba_wyw

liczba = int(input('Wpisz liczbę: '))
wynik, liczba_wywolan = przestaw(liczba)
print(f'Wynik: {wynik}, liczba wywołań: {liczba_wywolan}')
def rozbij():
    x = input("Podaj liczbę: ")
    n, a, x = len(x), 10 ** (len(x) - 1), int(x)
    for i in range(n):
        print(int(x // a), end = "   ")
        x, a  = x % a, a/10

rozbij()
n = int(input("Wpisz n:"))
suma_kwadratow = []

for i in range(n, 0, -1):
    if i*i <= n:
        n = n - i*i
        suma_kwadratow.append(f'{i}^2')

print(*suma_kwadratow)
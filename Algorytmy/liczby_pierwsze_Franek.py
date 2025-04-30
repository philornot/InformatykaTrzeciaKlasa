def liczby_pierwsze_1(n):
    lp = [1, 2]
    for i in range(3, n + 1):
        d = 0
        for j in range(2, i - 1):
            if i % j == 0:
                d += 1
        if d == 0:
            lp.append(i)
    return lp

print(liczby_pierwsze_1(1000))
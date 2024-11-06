def algorytm(n):
    s = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            s = s + 1
    return s

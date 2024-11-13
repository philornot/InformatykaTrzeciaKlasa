def algorytm(s, n=None):
    if not n:
        n = len(s)

    A = [0] * (n + 1)

    for i in range(1, n + 1):
        if s[i - 1] == 'a':
            A[i] = A[i - 1] + 1
        else:
            A[i] = A[i - 1]

    B = [0] * (n + 2)

    for j in range(n, 0, -1):
        if s[j - 1] == 'b':
            B[j] = B[j + 1] + 1
        else:
            B[j] = B[j + 1]

    k = 1

    for i in range(n + 1):
        if A[i] + B[i + 1] > k:
            k = A[i] + B[i + 1]

    return k


def wynik_algorytmu(s, n=None):
    k = algorytm(s, n)
    print(f'{s} --> {k}')

def F(n):
    s = 0
    if n == 1 or n == 2:
        s += n
    else:
        s += n*F(n - 2)
        print(n)
    return s*(n+1)

print(F(11))
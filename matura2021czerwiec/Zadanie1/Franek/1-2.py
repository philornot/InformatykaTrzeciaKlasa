def rk(n):
    dl = 0
    i = n//4
    while n > 0:
        if n - (i * i) >= 0:
            dl += 1
            n = n - (i * i)
        if n - (i*i) < 0:
            i -= 1
    return dl

print(rk(32))
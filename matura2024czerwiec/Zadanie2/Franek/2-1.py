def F(x):
    if x == 0:
        return 0
    if x >= 0:
        return 2 + F(x//2)

print(16)
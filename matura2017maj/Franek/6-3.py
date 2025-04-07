from main import dane
l = dane()

def abs(a):
    if a >= 0:
        return a
    else:
        return -1 * a

wyn = 0

for i in range(1,200,2):
    if abs(l[i][0] - l[i-1][0]) >= 128:
        wyn += 1
    for j in range(1,320):
        if abs(l[i][j] - l[i][j - 1]) >= 128:
            wyn += 1
        if abs(l[i][j] - l[i - 1][j]) >= 128:
            wyn += 1


print(wyn)
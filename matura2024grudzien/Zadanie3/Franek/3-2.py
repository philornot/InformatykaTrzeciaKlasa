from main import dane

l = dane()
lp, a = [1, 2], 2
while len(lp) <= 150:
    a += 1
    for i in range(2, a):
        print(a)
        if a % i == 0:
            break
    lp.append(a)
def c5dp(a):
    x = 0
    for i in range(len(lp)):
        if a % lp[i] == 0:
            x += 1
    if x >= 5:
        return True
    else:
        return False

wyn = []
for i in range(2000):
    if c5dp(l[i]) is True:
        wyn.append(l[i])

print(lp)
print(wyn)

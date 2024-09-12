def nieparzysty_skrot(n):
    n = str(n)
    m = ""
    for i in range(len(n)):
        if int(n[i]) % 2 != 0:
            m += n[i]
    if len(m) > 0:
        return int(m)
    else:
        return "Taki skrót nie istnieje"


LSk = list(open("../../../skrot.txt", "r"))
for i in range(len(LSk)):
    LSk[i] = int(LSk[i].strip())

wyn = []

for i in range(len(LSk)):
    a = LSk[i]
    b = nieparzysty_skrot(LSk[i])
    if a % 7 == 0 and b % 7 == 0 and a % 11 != 0 and b % 11 != 0:
        wyn.append(a)

for i in range(len(wyn)):
    print(wyn[i])

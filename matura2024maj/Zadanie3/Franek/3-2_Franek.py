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


LSkrot = list(open("matura2024maj/dane2024maj/skrot.txt", "r"))
for i in range(len(LSkrot)):
    LSkrot[i] = int(LSkrot[i].strip())

wyn = []
for i in range(len(LSkrot)):
    a = LSkrot[i]
    if nieparzysty_skrot(LSkrot[i]) == "Taki skrót nie istnieje":
        wyn.append(int(LSkrot[i]))
print(len(wyn)), print(max(wyn))

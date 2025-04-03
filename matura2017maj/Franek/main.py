def dane():
    l = list(open("../DANE/dane.txt", "r"))
    wyn = []
    for i in range(len(l)):
        l[i], tm = l[i].strip(), []
        l[i] += " "
        a = ""
        for j in range(len(l[i])):
            if l[i][j] != " ":
                a += l[i][j]
            else:
                tm.append(int(a))
                a = ""
        wyn.append(tm)
    return wyn


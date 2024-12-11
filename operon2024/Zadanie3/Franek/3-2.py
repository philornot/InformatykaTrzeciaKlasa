ltm, l = list(open("../../DaneOP/szyfrogram.txt", "r")), []
for i in range(len(ltm)):
    ltm[i] = ltm[i].strip()
for i in range(len(ltm)):
    tm = []
    for j in range(len(ltm[i])):
        if ltm[i][j] != " ":
            tm.append(int(ltm[i][j]))
        else:
            tm.append(ltm[i][j+1:-1])
            break
    l.append(tm)
print(l)

def szyfr(n, s):
    lwyn = []
    for i in range(len(l-n)):
        tm = ""
        while len(tm) < n:

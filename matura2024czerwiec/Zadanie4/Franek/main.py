def przesyl_pakietow(l):
    tabwyn = [l]
    ltc = l
    for i in range(len(l)-1):
        lzm = [""] * len(l)
        for j in range(len(l)):
            lzm[j] = ltc[l[j]-1]
        ltc = lzm
        tabwyn.append(ltc)
    return tabwyn

def lista():
    l = list(open("../../dane2024czerwiec/odbiorcy.txt","r"))
    for i in range(len(l)):
        l[i] = int(l[i].strip())
    return l

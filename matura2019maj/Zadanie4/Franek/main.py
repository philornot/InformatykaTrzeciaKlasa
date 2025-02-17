def dane():
    l = list(open("../../dane2019maj/liczby.txt","r"))
    for i in range(500):
        l[i] = l[i].strip()
    return l

def czy_p_3(a):
    while(a > 1):
        if a % 3 == 0:
            a = a/3
        else:
            return "Nie"
    return "Tak"

def silnia(a):
    if a == 0:
        return 1
    else:
        wyn = 1
        for i in range(a):
            wyn = wyn * (i + 1)
    return wyn

def sum_sil(s):
    wyn = 0
    for i in range(len(s)):
        wyn += silnia(int(s[i]))
    return wyn

def nwd(a, b):
    return 0
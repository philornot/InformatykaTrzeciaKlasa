from main import dane1, dane2
l1 = dane1()
l2 = dane2()

def str_to_l(s):
    l = []
    s += " "
    a = ""
    for i in s:
        if i == " ":
            l.append(int(a))
            a = ""
        else:
            a += i
    return l

def p_i_n(l):
    wyn = []
    for i in l:
        if i % 2 == 0:
            wyn.append("P")
        else:
            wyn.append("N")
    if wyn.count("P") == 5 and wyn.count("N") == 5:
        return 1
    else:
        return 0

wyn = 0
for i in range(1000):
    lista1 = str_to_l(l1[i])
    lista2 = str_to_l(l2[i])
    if p_i_n(lista1) == 1 and p_i_n(lista2) == 1:
        wyn += 1

print(wyn)
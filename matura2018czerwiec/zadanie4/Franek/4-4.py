from main import dane1, dane2
l1 = dane1()
l2 = dane2()
odp = []

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

for i in range(1000):
    tm = l1[i] + " " + l2[i]
    tm = sorted(str_to_l(tm))
    stm = ''
    for i in range(len(tm)):
        stm += str(tm[i])
        stm += " "
    odp.append(stm[0:-1])

print(odp)
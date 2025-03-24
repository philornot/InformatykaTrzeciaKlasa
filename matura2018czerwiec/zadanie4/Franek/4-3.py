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

for i in range(1000):
    l1[i] = str_to_l(l1[i])
    l2[i] = str_to_l(l2[i])

wyn = []
for i in range(1000):
    lis1 = list(set(l1[i]))
    lis2 = list(set(l2[i]))
    ile = 0
    if len(lis1) == len(lis2):
        for j in range(len(lis1)):
            if lis1[j] == lis2[j]:
                ile += 1
        if ile == len(lis1):
            wyn.append(i + 1)

print(wyn)
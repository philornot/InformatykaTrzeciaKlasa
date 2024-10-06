L = list(open("../../../matura2024maj/dane2024maj/liczby.txt", "r"))
L[0] = L[0] + " "
L[1] = L[1] + " "
L1 = []
L2 = []
a = ""
for i in range(len(L[0])):
    if L[0][i] == " ":
        L1.append(int(a.strip()))
        a = ""
    else:
        a = a + L[0][i]

b=''
for i in range(len(L[1])):
    if L[1][i] == " ":
        L2.append(int(b))
        b = ""
    else:
        b = b + L[1][i]


from main import dane, nwd_listy

l = dane()
pl, dl, nwdc = 0, 1, 0

i, tm = 0, []
odp = []
while i < len(l):
    tm.append(int(l[i]))
    if nwd_listy(tm) > 1:
        if len(tm) > len(odp):
            odp = tm
            print("+")
    else:
        tm = [int(l[i])]
        print(i)
    i += 1

print(len(odp), odp[0], nwd_listy(odp))
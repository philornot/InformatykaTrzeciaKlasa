def tab():
    L = list(open("../../dane2023maj/pi.txt","r"))
    for i in range(len(L)):
        L[i] = L[i].strip()
    return L

def dublet(L):
    lwyn = []
    for i in range(len(L)-1):
        lwyn.append(str(L[i])+str(L[i+1]))
    return lwyn

def czyrm(L):
    cr = [L[0]]
    i = 1
    while L[i] > L[i-1]:
        cr.append(L[i])
        i += 1
    cm = L[i::]
    return cr, cm

print(czyrm([2, 5, 7, 9, 8, 3, 1]))
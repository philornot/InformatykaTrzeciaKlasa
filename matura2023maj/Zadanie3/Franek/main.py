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

def dane1():
    l1 = list(open("../../DANE/dane1.txt","r"))
    for i in range(len(l1)):
        l1[i] = l1[i].strip()
    return l1

def dane2():
    l2 = list(open("../../DANE/dane2.txt","r"))
    for i in range(len(l2)):
        l2[i] = l2[i].strip()
    return l2
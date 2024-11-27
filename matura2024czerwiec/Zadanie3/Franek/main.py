def lista():
    l = list(open("../../dane2024czerwiec/slowa.txt","r"))
    for i in range(len(l)):
        l[i] = l[i].strip()
    return l

def ROT13(s):
    S = ""

def lista():
    l = list(open("../../dane2024czerwiec/slowa.txt","r"))
    for i in range(len(l)):
        l[i] = l[i].strip()
    return l

def ROT13(s):
    S = ""
    for i in range(len(s)):
        if ord(s[i]) < 110 and ord(s[i]) >= 97:
            S += chr(ord(s[i])+13)
        else:
            S += chr(ord(s[i]) - 13)
    return S


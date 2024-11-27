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

def czy_pol(s):
    l1 = []
    l2 = []
    for i in range(len(s)):
        if s[i] not in l1:
            l1.append(s[i])
            l2.append(s.count(s[i]))
    if max(l2) >= (len(s)/2):
        return True
    else:
        return False

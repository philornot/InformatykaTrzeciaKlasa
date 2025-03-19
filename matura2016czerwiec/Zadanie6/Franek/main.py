def dane():
    l = list(open("../../dane2016czerwiec/liczby.txt", "r"))
    for i in range(len(l)):
        l[i] = l[i].strip()

    return l

def dane():
    l = list(open("../../dane2024grudzien/liczby.txt", "r"))
    for i in range(2000):
        l[i] = int(l[i].strip())
    return l
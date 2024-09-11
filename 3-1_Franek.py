def nieparzysty_skrot():
    n = input()
    m = ""
    for i in range(len(n)):
        if int(n[i]) % 2 != 0:
            m += n[i]
    if len(m) > 0:
        return(int(m))
    else:
        return("Taki skrót nie istnieje")

print(nieparzysty_skrot())
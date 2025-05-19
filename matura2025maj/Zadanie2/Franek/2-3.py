l = list(open("../../dane2025maj/symbole.txt", "r"))
for i in range(len(l)):
    l[i] = l[i].strip()

for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j] == "o":
            l[i][j] = "0"
        if l[i][j] == "+":
            l[i][j] = "1"
        if l[i][j] == "*":
            l[i][j] = "2"

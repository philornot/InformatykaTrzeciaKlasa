l = list(open("../../dane2025maj/symbole_przyklad.txt", "r"))
for i in range(len(l)):
    l[i] = l[i].strip()

wyn, x = [], 1
for i in range(1, len(l) - 1):
    for j in range(1, len(l[i]) - 1):
        if l[i][j] == l[i][j - 1] and l[i][j] == l[i][j + 1]:
            if l[i][j - 1: j + 1] == l[i - 1][j - 1: j + 1] and l[i][j - 1: j + 1] == l[i + 1][j - 1: j + 1]:
                wyn.append([x, i + 1, j + 1])
                x += 1

for i in range(len(wyn)):
    for j in range(3):
        print(wyn[i][j], end=" ")
    print(" ")
from main import lista
l = lista()
wyn = 0

for i in range(len(l)):
    for j in range(len(l[i])-2):
        if l[i][j] == "k" and l[i][j+2] == "t":
            wyn += 1

print(wyn)
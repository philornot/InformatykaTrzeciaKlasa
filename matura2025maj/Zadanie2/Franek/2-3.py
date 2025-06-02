l = list(open("../../dane2025maj/symbole.txt", "r"))
for i in range(len(l)):
    l[i] = l[i].strip()

l2 = []
for i in range(len(l)):
    a = list(l[i])
    for j in range(len(a)):
        if a[j] == "o":
            a[j] = "0"
        if a[j] == "+":
            a[j] = "1"
        if a[j] == "*":
            a[j] = "2"
    l2.append("")
    for x in a:
        l2[i] += x

print(l2)
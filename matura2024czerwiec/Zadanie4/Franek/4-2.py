from main import lista
l, wyn = lista(), 0

for i in range(1, len(l)):
    if i not in l:
        wyn += 1

print(wyn)
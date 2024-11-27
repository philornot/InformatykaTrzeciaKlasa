from main import lista, ROT13
l = lista()
wyn = 0
lwyn = []

for i in range(len(l)):
    if ROT13(l[i]) == l[i][::-1]:
        wyn += 1
        lwyn.append(l[i])

print(wyn)
lmax = len(lwyn[0])
slmax = l[0]
for i in range(1,wyn):
    if len(lwyn[i]) > lmax:
        lmax = len(lwyn[i])
        slmax = lwyn[i]

print(slmax)
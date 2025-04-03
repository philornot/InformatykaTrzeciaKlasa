from main import dane
l = dane()

najw, najm = max(l[0]), min(l[0])
for i in range(1,len(l)):
    if max(l[i]) > najw:
        najw = max(l[i])
    if min(l[i]) < najm:
        najm = min(l[i])

print(najw, najm)
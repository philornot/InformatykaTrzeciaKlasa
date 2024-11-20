from main import tab, dublet

def zad31():
    spr = dublet(tab())
    wyn = 0
    for i in range(len(spr)):
        if int(spr[i]) > 90:
            wyn += 1
    return wyn

print(zad31())
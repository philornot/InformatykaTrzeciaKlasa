def przesyl_pakietow(l):
    tabwyn = [l]
    for i in range(len(l)):
        lzm = [""] * len(l)
        for j in range(len(l)):
            lzm[j] = l[l[j]-1]
            print(l[l[j]-1], l[j])
        tabwyn.append(lzm)
        l = lzm
        print(lzm)
    return tabwyn

print(przesyl_pakietow([4, 3, 5, 3, 1, 2]))
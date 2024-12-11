def szyfr(n, s):
    lwyn = []
    for i in range(len(s)-n+1):
        tn = (s[i:i+n])
        if tn not in lwyn:
            lwyn.append(tn)
    return sorted(lwyn)

print(szyfr(3, "zzzaaabbbccc"))
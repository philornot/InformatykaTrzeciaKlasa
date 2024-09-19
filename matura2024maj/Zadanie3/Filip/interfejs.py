def nieparz_skrot(n):
    m_list = []
    n = n.strip()
    for char in str(n):
        if int(char) % 2 == 1:
            m_list.append(char)

    m = ''.join(m_list)
    if m == '':
        return None  # liczba n nie ma nieparzystego skrótu
    else:
        m = int(m)
    return m


def nieparz_skrot_plik(plik):
    with open(plik, encoding="utf-8") as f:
        lines = f.readlines()
    np = {}
    for i in lines:
        np[int(i.strip())] = nieparz_skrot(i)
    return np

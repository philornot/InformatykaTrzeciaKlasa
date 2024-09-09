def nieparz_skrot(n):
    m_list = []
    for char in str(n):
        if int(char) % 2 == 1:
            m_list.append(char)

    m = ''.join(m_list)
    if m == '':
        return None  # liczba n nie ma nieparzystego skrótu
    else:
        m = int(m)
    return m
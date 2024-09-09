def nieparz_skrot(n):
    m_list = []
    for char in str(n):
        if int(char) % 2 == 1:
            m_list.append(char)

    m = int(''.join(m_list))
    print(f'Nieparzysty skrót liczby {n} to {m}')


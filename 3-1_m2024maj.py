n = 31034
m_list = []

for char in str(n):
    if int(char) % 2 == 1:
        print(f'{char} jest nieparzyste - dodaję {char} do listy...')
        m_list.append(char)
    elif int(char) % 2 == 0:
        print(f'{char} jest parzyste')

print(f'\nm_list: {m_list}\n')

for num in m_list:
    
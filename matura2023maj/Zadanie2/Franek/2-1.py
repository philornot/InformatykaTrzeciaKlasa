from main import ile_bloków

def ile_bloków2(n):
    N = bin(n)[2::]
    return ile_bloków(N)

print(ile_bloków2(245))
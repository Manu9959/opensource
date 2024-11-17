X, Y, Z = map(int, input().split())

if Y >= Z:
    print(0)
else:
    max_mangoes = (Z - Y) // X
    print(max_mangoes)

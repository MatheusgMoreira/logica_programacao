matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in matriz:
    for valor in linha:
        print(valor, end=' ')
    print()  # quebra linha após cada linha da matriz

"""2 - Faça um programa que gere a matriz abaixo
[0, 1, 0, 1, 0, 1, 0, 1]
[0, 1, 0, 1, 0, 1, 0, 1]
[0, 1, 0, 1, 0, 1, 0, 1]
[0, 1, 0, 1, 0, 1, 0, 1]
[0, 1, 0, 1, 0, 1, 0, 1]
[0, 1, 0, 1, 0, 1, 0, 1]
[0, 1, 0, 1, 0, 1, 0, 1]
[0, 1, 0, 1, 0, 1, 0, 1]"""

matriz = []
for i in range(8):
    linha = []
    for j in range(0, 8, 1):
        if j % 2 == 0:
            linha.append(0)
        else:
            linha.append(1)
        matriz.append(linha)
for i in range(8):
    print(matriz[i])

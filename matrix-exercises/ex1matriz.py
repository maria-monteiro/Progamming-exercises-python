"""1 – Faça um programa que gere a matriz abaixo.
0, 0, 0, 0, 0, 0, 0, 0
1, 1, 1, 1, 1, 1, 1, 1
0, 0, 0, 0, 0, 0, 0, 0
1, 1, 1, 1, 1, 1, 1, 1
0, 0, 0, 0, 0, 0, 0, 0
1, 1, 1, 1, 1, 1, 1, 1
0, 0, 0, 0, 0, 0, 0, 0
1, 1, 1, 1, 1, 1, 1, 1"""

matriz = []
for i in range(8):
    if i % 2 == 0:
        matriz.append([0] * 8)
    else:
        matriz.append([1] * 8)
for i in range(len(matriz)):
    print(matriz[i])
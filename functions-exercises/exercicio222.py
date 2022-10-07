"""2 – Gere uma lista de 30 números aleatórios entre 1 e 100. Não pode haver número repetido
na lista."""
from random import randint


def verificar_numero_lista(nro_procurado, lista):
    existe = False
    for numero in lista:
        if numero == nro_procurado:
            existe = True
    return existe


lista = []
for numero in range(0, 30):
    nro = randint(1, 100)
    while verificar_numero_lista(nro, lista):
        nro = randint(1, 100)
    lista.append(nro)
print(lista)

"""Faça um programa para informatizar o cadastro de produtos em uma loja. Você deve:
- cadastrar os produtos com as seguintes informações: nome do produto, valor, fornecedor e quantidade em estoque.
Não deve ser permitido cadastrar produtos com mesmo nome. Obs: Diferenciar maiúsculas e minúscula.
- informar o percentual de produtos que custam mais de R$ 100,00.
- permitir a atualização do valor do produto. Usuário deve digitar o nome do produto e depois atualizar os valores.
Caso o produto não esteja cadastrado, informar isso ao usuário.
- preço médio dos produtos da SAMSUNG.
- nome do produto mais caro dentre produtos da SAMSUNG.
- qual o total de itens no estoque.
- listar os produtos por fabricante. Dica: criar a lista de fabricantes sem repetição e depois percorrê-la exibindo os produtos.
- cadastrar uma venda salvando: nome do ciente, nome do produto e valor do produto.
Considere que só pode ser vendido um produto por vez. Só podem ser feitas vendas de produtos cadastrados.
- listar as vendas"""


def verificar_se_existe(dado, matriz, coluna):
    for i in range(len(matriz)):
        if matriz[i][coluna] == dado:
            return True
        return False


def verificar_mais_caro(matriz, fornecedor, coluna_valor=1, coluna_fornecedor=2, coluna_nome=0):
    valor_mais_caro = -1
    nome_mais_caro = ''
    for i in range(len(matriz)):
        if matriz[i][coluna_fornecedor].upper() == fornecedor.upper():
            if matriz[i][coluna_valor] > valor_mais_caro:
                valor_mais_caro = matriz[i][coluna_valor]
                nome_mais_caro = matriz[i][coluna_nome]
    return nome_mais_caro


def verificar_total_itens(matriz, coluna_qtdd=3):
    cont_qtdd = 0
    for i in range(len(matriz)):
        if matriz[i][coluna_qtdd] > 0:
            cont_qtdd += matriz[i][coluna_qtdd]
    return cont_qtdd

lista_vendas = []
cont_produtos = 0
lista_produtos = []
matriz = []
opcao = -1
while opcao != 0:
    print('MENU')
    print('1 - Cadastrar ')
    print('2 - Informar o percentual dos produtos que custam mais de 100R$ ')
    print('3 - Atualizar valor de um produto ')
    print('4 - Preço médio dos produtos SAMSUNG ')
    print('5 - Nome do produto mais caro da fornecedora SAMSUNG ')
    print('6 - Total de itens no estoque ')
    print('7 - Listar produtos por fornecedor')
    print('8 - Cadastrar venda')
    print('9 - Listar vendas')
    opcao = int(input('Escolha uma opção '))

    if opcao == 1:
        nome = input('Nome: ')
        existe_nome_produto = verificar_se_existe(nome, matriz, 0)
        if existe_nome_produto:
            print('Nome já cadastrado.')
        if not existe_nome_produto:
            valor = float(input('Valor: '))
            fornecedor = input('Fornecedor: ')
            qtdd = int(input('Qtdd: '))
            lista_produtos = [nome, valor, fornecedor, qtdd]
            matriz.append(lista_produtos)
            cont_produtos += 1

    elif opcao == 2:
        cont_produtos_mais_100 = 0
        for i in range(len(matriz)):
            if matriz[i][1] > 100:
                cont_produtos_mais_100 += 1
        print(f'A média de produtos de custam mais de 100R$ é {cont_produtos_mais_100 / cont_produtos * 100:.2f}%.' if cont_produtos > 0 else 'Não há produtos cadastrados.')

    elif opcao == 3:
        nome = input('Nome do produto que deseja atualizar: ')
        existe_nome_produto = False
        for i in range(len(matriz)):
            if matriz[i][0] == nome:
                existe_nome_produto = True
                valor_atualizado = float(input('Digite o novo valor: '))
                matriz[i][1] = valor_atualizado
                print('Valor atualizado com sucesso.')
        if not existe_nome_produto:
            print('Nome não cadastrado.')

    elif opcao == 4:
        existe_fornecedor = verificar_se_existe('samsung', matriz, 1)
        soma_produtos_samsung = 0
        cont_produtos_samsung = 0
        if existe_fornecedor:
            for i in range(len(matriz)):
                if matriz[i][2].upper() == 'samsung'.upper():
                    existe_fornecedor = True
                    soma_produtos_samsung += matriz[i][1]
                    cont_produtos_samsung += 1
        else:
            print('Fornecedor não cadastrado.')
        print(f'A média dos produtos da SAMSUNG é {soma_produtos_samsung / cont_produtos_samsung}'if cont_produtos_samsung > 0 else 'Não há fornecedor SAMSUNG')

    elif opcao == 5:
        existe_fornecedor = verificar_se_existe('samsung', matriz, 2)
        if existe_fornecedor:
            nome_mais_caro = verificar_mais_caro(matriz, 'samsung')
            print(nome_mais_caro)

    elif opcao == 6:
        total_itens = verificar_total_itens(matriz)
        print(total_itens)

    elif opcao == 7:
        lista_fabricantes = []
        for i in range(len(matriz)):
            if matriz[i][2] not in lista_fabricantes:
                lista_fabricantes.append(matriz[i][2])

        for indice in range(len(lista_fabricantes)):
            print(f'FORNECEDOR : {lista_fabricantes[indice]}')
            for i in range(len(matriz)):
                if matriz[i][2] == lista_fabricantes[indice]:
                    print(f'nome:  {matriz[i][0]}')
                    print(f'valor:  {matriz[i][1]}')
                    print(f'qtdd estoque:  {matriz[i][3]}')

    elif opcao == 8:
        # só pode ser feita uma venda por vez e só podem ser vendidos produtos cadastrados
        nome_cliente = input('Digite seu nome: ')
        nome_produto = input('Digite o nome do produto: ')
        existe = verificar_se_existe(nome_produto, matriz, 0)
        if existe:
            valor_produto = input('Digite o valor do produto: ')
            lista_venda = [nome_cliente, nome_produto, valor_produto]
        elif not existe:
            print('Esse produto não consta no sistema.')

    elif opcao == 9:
        for i in range(len(lista_vendas)):
            print(lista_vendas[i])






'''Dicionários (Estruturas de Dados)
Crie um dicionário chamado estoque onde as chaves são nomes de produtos (strings) e os valores são as quantidades em estoque (inteiros).


Adicione um novo produto ao dicionário.

Use um loop para iterar sobre o dicionário e imprimir cada par de chave e valor no formato: "O produto [Chave] tem [Valor] unidades em estoque."'''

estoque = {
    'Maçã': 50, 'Banana': 30, 'Laranja': 20,'Uva': 15,'Pera': 25,'Manga': 10,'Abacaxi': 5}

estoque['Kiwi'] = 12

for produto, quantidade in estoque.items():
    print(f'O produto {produto} tem {quantidade} unidades em estoque.')
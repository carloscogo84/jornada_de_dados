# Atualização de Dados - Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

produtos = [
    {'id': 1, 'nome': 'teclado', 'preco': 400},
    {'id': 2, 'nome': 'violão', 'preco': 500},
    {'id': 3, 'nome': 'guitarra', 'preco': 800},
]

for i in produtos:
    print(i)

print()

for produto in produtos:
    if produto['id'] == 1:
        produto['preco'] = 600

for i in produtos:
    print(i)

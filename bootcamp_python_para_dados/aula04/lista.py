# Lista - ordenada
produto: str = "Sapato"
produto_2: str = "Camiseta"
produto_3: str = "Video Game"

produtos: list = []

# append() - adiciona
produtos.append(produto)
produtos.append(produto_2)
produtos.append(produto_3)

print(produtos)

# pop() - remove o ultimo produto que entrou (performance maior)
produtos.pop()
print(produtos)

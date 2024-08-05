# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista_compras: list = ["maçã", "banana", "cereja"]
precos: float = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total: float = sum(precos[item] for item in lista_compras)
print(f"Preço total: {total}")

import json
# Dicionario

produto_01: dict = {
    "nome": "sapato",
    "quatidade": "39",
    "preco": 10.38,
    "disponibilidade": True
}

produto_02: dict = {
    "nome": "televisao",
    "quantidade": 10,
    "preco": 70.38,
    "disponibilidade": False
}

carrinho: list = []
carrinho.append(produto_01)
carrinho.append(produto_02)

print(carrinho)

print("-----")

# DICT TO JSON
# json é o dicionario do javascript
# 1 - fazer import da biblioteca json
carrinho_json = json.dumps(carrinho)
print(carrinho_json)

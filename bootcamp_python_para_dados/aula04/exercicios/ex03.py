# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

from typing import Dict, Any

livro_01: Dict[str, Any] = {
    "titulo": "O monte",
    "autor": "Carlos",
    "ano": 2020
}

livro_02: Dict[str, Any] = {
    "titulo": "A grande sacada",
    "autor": "Karen",
    "ano": 2024
}

print(livro_01)

print("-----")

# Transformando o dicionario em uma lista
lista_de_elementos: list = livro_01.items()

for elemento in lista_de_elementos:
    print(elemento)

print("-----")

lista_de_livros = []
lista_de_livros.append(livro_01)
lista_de_livros.append(livro_02)

for livro in lista_de_livros:
    print(livro)

print("---")

lista_de_livros_usando_dict: dict = {
    "livro_01": {
        "titulo": "O monte",
        "autor": "Carlos",
        "ano": 2020},

    "livro_02": {
        "titulo": "A grande sacada",
        "autor": "Karen",
        "ano": 2024}

}
for i in lista_de_livros_usando_dict:
    print(i)

for i in lista_de_livros_usando_dict.items():
    print(i)

print(lista_de_livros_usando_dict['livro_01'])
print(lista_de_livros_usando_dict['livro_01']['autor'])

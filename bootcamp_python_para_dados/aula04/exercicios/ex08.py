# Ordenação Personalizada - Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas: list = [
    {"nome": "Pedro", "idade": 40},
    {"nome": "Clovis", "idade": 30},
    {"nome": "Tiago", "idade": 20}
]

pessoas.sort(key=lambda pessoa: pessoa["nome"])
print(pessoas)

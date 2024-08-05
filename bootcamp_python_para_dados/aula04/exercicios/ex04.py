# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

def contar_caracteres(c):
    contagem = {}
    for caractere in c:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem


print(contar_caracteres("engenharia de dados"))

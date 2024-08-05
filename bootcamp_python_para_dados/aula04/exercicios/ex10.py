# Divisão de Dados em Grupos - Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

numeros: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares: list = [valor for valor in numeros if valor % 2 == 0]
impares: list = [valor for valor in numeros if valor % 2 != 0]
print("Valores pares", pares)
print("Valores impares", impares)

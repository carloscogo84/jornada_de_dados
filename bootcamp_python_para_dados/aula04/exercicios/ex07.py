# Filtragem de Dados - Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

idades: list = [22, 15, 30, 17, 18]
idades_valisdas: list = [idade for idade in idades if idade >= 18]
print(idades_valisdas)

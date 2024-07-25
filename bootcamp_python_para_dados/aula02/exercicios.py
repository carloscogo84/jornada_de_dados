import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
numero_1 = int(input("Digite um número inteiro: "))
numero_2 = int(input("Digite outro número inteiro: "))
soma = numero_1 + numero_2
print(f"Os números somados totalizam {soma}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero = int(input("Insira um número: "))
resto_divisao = numero % 5
print("O resto da divisão por 5 é:", resto_divisao)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))
resultado_multiplicacao = numero_1 * numero_2
print("O resultado da multiplicação é:", resultado_multiplicacao)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
numero_1 = int(input("Digite o primeiro número inteiro: "))
numero_2 = int(input("Digite o segundo número inteiro: "))
divisao_inteira = numero_1 // numero_2
print(f"A divisão inteira é {divisao_inteira}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero = int(input("Informe um número: "))
resultado_quadrado = numero ** 2
print("O quadrado do número é:", resultado_quadrado)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
numero_1 = float(input("Digite um número: "))
numero_2 = float(input("Digite outro número: "))
soma = numero_1 + numero_2
print("O resultado da soma é", soma)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numero_1 = float(input("Digite um número: "))
numero_2 = float(input("Digite outro número: "))
resultado_media = (numero_1 + numero_2) / 2
print("A média é: ", resultado_media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
potencia = base ** expoente
print("O resultado da potência é:", potencia)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
Fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {Fahrenheit}°F")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio_do_circulo = float(input("Digite o valor do raio: "))
area_do_circulo = math.pi * raio_do_circulo ** 2
print(f"{area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto = input("Digite um texto: ")
texto_maiusculas = texto.upper()
print("Texto em maiúsculas:", texto_maiusculas)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input("Digite seu nome completo: ")
nome_minusculo = nome.lower()
print("Nome maiúsculo:", nome_minusculo)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")
frase_sem_espaco = frase.strip()
print("Frase sem espaços no início e no final:", frase_sem_espaco)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data_usuario = input("Digite uma data no valor dd/mm/aaaa: ")
lista_dia_mes_ano = data_usuario.split("/")
print(f"O elemento 1 é o: {lista_dia_mes_ano[0]}")
print(f"O elemento 1 é o: {lista_dia_mes_ano[1]}")
print(f"O elemento 1 é o: {lista_dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
frase_1 = input("Digite um texto: ")
frase_2 = input("Digite outro texto: ")
texto = frase_1 + frase_2
print("Texto concatenado:", texto)


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
valor1 = True
valor2 = False
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
valor1 = True
valor2 = False
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))

resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))
resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação

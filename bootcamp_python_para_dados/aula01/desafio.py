CONSTANTE_BONUS = 1000
# 1) Solicita ao usuário que digite seu nome
nome = input("Digite seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

salario = input("Informe seu salario: ")
salario = float(salario)

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

bonus = input("Informe a porcentagem do bonus recebido: ")
bonus = float(bonus)

# 4) Calcule o valor do bônus final
valor_bonus = CONSTANTE_BONUS + salario * bonus

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Olá {nome}, seu salário é de R$ {salario} e seu bonus é de R$ {valor_bonus}")

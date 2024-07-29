# 1) Solicita ao usuário que digite seu nome
nome_usuario = input("Digite seu nome: ")

if nome_usuario.isdigit():
    print("Você digitou seu nome errado")
    exit()
elif len(nome_usuario) == 0:  # Verificando se o número de caractere for zero
    print("Você não digitou nada")
    exit()
elif nome_usuario.isspace():
    print("Você digitou somente espaços")
    exit()

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante


# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante


# 4) Calcule o valor do bônus final


# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

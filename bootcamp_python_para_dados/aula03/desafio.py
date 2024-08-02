# Inicializa as variáveis para o controle do loop
nome_valido = False
salario_valido = False
bonus_valido = False

# Loop para verificar o nome
while not nome_valido:
    try:
        nome = input("Digite seu nome: ")
        if len(nome) == 0:
            raise ValueError("Seu nome não pode estar vazio.")
        elif nome.isspace():
            raise ValueError("Você digitou somente espaços")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não pode conter digitos")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:
        print(e)

# Loop para verificar o salário
while not salario_valido:
    try:
        salario = float(input("Informe o valor do salário: "))
        if salario < 0:
            print("Informe um valor positivo para o salário")
        else:
            salario_valido = True
    except ValueError:
        print("Entrada inválida para o salário, informe um número")

# Loop para verificar o bônus
while not bonus_valido:
    try:
        bonus = float(input("Informe o valor do bonus: "))
        if bonus < 0:
            print("Informe o valor positivo para o bonus")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada inválida, por favor digite um número")

bonus_recebido = 1000 + salario * bonus

# Imprime as informações para o usuário
print(f"{nome}, seu salário é R${
      salario:.2f} e seu bonus final é R${bonus_recebido:.2f}.")

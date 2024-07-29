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

print()

try:
    nome = input("Informe seu nome: ")
    # verifica se o nome está vazio
    if len(nome) == 0:
        raise ValueError("O seu nome não pode estar vazio")
    # verifica se há caracteres no nome
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não pode ter números")
    # verifica se digitou espaços
    elif nome.isspace():
        raise ValueError("Voce3 digitou somente espaços")
    else:
        print(f"Nome válido: {nome}")

except ValueError as e:
    print(e)

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario = float(input("Informe su salário: "))
    if salario < 0:
        print("Informe um valor positivo")
    else:
        print("Seu salário é de R$", salario)
except ValueError:
    print("Entrada inválida, por favor informe um número")

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

try:
    bonus_recebido = float(input("Informe o bonus recebido: "))
    if bonus_recebido < 0:
        print("Informe um valor positivo para o bonus")
    else:
        print("Valor do bonus:", bonus_recebido)

except ValueError:
    print("Entrada informada inválida")


# 4) Calcule o valor do bônus final e KPI
bonus_final = bonus_recebido * 1.2  # Exemplo, ajuste conforme necessário
kpi = (salario + bonus_final) / 1000  # Exemplo simples de KPI

print(f"Seu KPI é de R${kpi:.2f}")
print(f"Seu salário é de R${
      salario:.2f} e seu bonus final é de R${bonus_final:.2f}")

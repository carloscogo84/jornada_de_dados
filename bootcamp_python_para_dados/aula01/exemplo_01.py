# Função que mostra algo pro usuário
# Strings usam " " ou ''.
print("Hello World!")

# Somando números
print(3 + 7)

# Concatenando strings
print("Olá" + " " + "turma")
print("Olá " + "turma")

# Input - solicitando algo do usuário
print(input('Digite seu nome: '))

print("Olá " + input("Qual seu nome? ") + "!")

# Digitando o nome e retornando o numero de caracteres
nome = input("Digite seu nome: ")
quantidade_caracteres = len(nome)
print(quantidade_caracteres)

# Criar um programa onde o usuário digite dois valores e apareça a soma

numero1 = input('Digite o primeiro valor: ')
numero2 = input('Digite o segundo valor: ')

numero1 = int(numero1)
numero2 = int(numero2)

print(numero1 + numero2)

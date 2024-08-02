# try-except e if

try:
    numero_1 = int(input("Digite um número inteiro: "))
    numero_2 = int(input("Digite outro número inteiro: "))
    resultado = numero_1 / numero_2
    print(resultado)
except ZeroDivisionError:
    print('integer division or modulo by zero')
except KeyboardInterrupt:
    print("Acho que você não quis inserir um número")


try:
    resultado = len("Luciano")
    print(resultado)
except TypeError as e:
    print(e)  # imprime a mensagem de erro
else:
    print("Tudo ocorreu bem")
finally:
    print("O importante é participar")


# if diferente do try, ele checa primeiro
numero = int(input("Insira um número: "))
if isinstance(numero, int):  # isinstance verifica a variavel
    print("A variável é um inteiro.")
else:
    print('A variável não é um inteiro')

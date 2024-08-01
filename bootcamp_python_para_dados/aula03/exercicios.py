# Exercício 1: Verificação de Qualidade de Dados

# Você está analisando um conjunto de dados de vendas e precisa garantir
# que todos os registros tenham valores positivos para `quantidade` e `preço`.
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos
# forem positivos ou "Dados inválidos" caso contrário.

# preciso avaliar sa variaveis quantidade e preço
quantidade = 40
preco = 20

if quantidade > 0 and preco > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")


# Exercício 2: Classificação de Dados de Sensor

# Imagine que você está trabalhando com dados de sensores IoT.
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

temperatura = float(input("Informe a temperatura: "))

if temperatura < 15:
    print("Baixa")
elif 15 <= temperatura <= 25:
    print("Normal")
else:
    print("Alta")


# Exercício 3: Filtragem de Logs por Severidade

# Você está analisando logs de uma aplicação e precisa filtrar mensagens
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`,
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
log = {'timestamp': '2021-06-23 10:00:00',
       'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] == "ERROR":
    print(log['message'])

# Exercício 4: Validação de Dados de Entrada

# Antes de processar os dados de usuários em um sistema de recomendação,
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha
# fornecido um email válido. Escreva um programa que valide essas condições
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
idade = int(input("Informe sua idade: "))
email = input("Informe seu email: ")

if not 18 <= idade <= 65:
    print("Idade fora do intervalo permitido")
elif "@" not in email or "." not in email:
    print("Email inválido")
else:
    print("Dados de usuários válidos")


# Exercício 5: Detecção de Anomalias em Dados de Transações

# Você está trabalhando em um sistema de detecção de fraude e precisa identificar
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h).
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
transacao = {'valor': 12000, 'hora': 20}

if transacao["valor"] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
    print("Transação supseita")
else:
    print("Transação normal")


# Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
texto = "Hoje é nossa segunda aula  do bootcamp , bootcamp de python"
novo_texto = texto.replace(",", "")
palavras = novo_texto.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1
    print(contagem_palavras)


# Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
numeros = [10, 20, 30, 40, 50]
minimo = min(numeros)
maximo = max(numeros)

normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]
print(normalizados)

print("----")


def normalizados(numeros):
    try:
        minimo = min(numeros)
        maximo = max(numeros)
        if minimo == maximo:
            return [0.5 for _ in numeros]
        dados_normalizados = [(x - minimo) / (maximo - minimo)
                              for x in numeros]
        return dados_normalizados
    except Exception as e:
        print(f"Ocorreu um erro {e}")
        return None


numeros = [10, 20, 30, 40, 50]
dados_normalizados = normalizados(numeros)
print(dados_normalizados)

# Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

usuarios = [
    {"nome": "Pedro", "email": 'pedro@yahoo.com'},
    {"nome": "Amanda", "email": ''},
    {"nome": "Jessica", "email": 'jessica@hotmail.com'}
]
usuarios_validos = [usuario for usuario in usuarios if usuario['email']]
print(usuarios_validos)

print("-----")


def filtrar_dados_faltantes(dados, campo):
    # Filtrar dicionários onde o campo específico está faltando ou é None
    dados_filtrados = [
        dado for dado in dados if campo in dado and dado[campo] is not None]
    return dados_filtrados


# Exemplo de uso
usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": None},
    {"nome": "Charlie"},
    {"nome": "David", "email": "david@example.com"}
]

campo_especifico = "email"
usuarios_filtrados = filtrar_dados_faltantes(usuarios, campo_especifico)
print(usuarios_filtrados)


# Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
numeros = range(1, 11)
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)


# Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# Exercícios com WHILE

# Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

# Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

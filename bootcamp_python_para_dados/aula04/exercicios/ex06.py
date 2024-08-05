# Eliminação de Duplicatas - Dada uma lista de emails, remover todos os duplicados.

emails: list = ["pedro@gmail.com", "caio@yahoo.com",
                "pedro@gmail.com", "clovis.hotmail.com"]

print(emails)

# set() - usado para encontrar elementos unicos
emails_unicos: list = list(set(emails))
print(emails_unicos)

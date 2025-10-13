import re

# Funções essenciais:

# re.search(padrao, texto) procura a primeira ocorrencia do padrão em uma string.
# re.findall(padrão, texto) retorna todas as ocorrencias do padrão em uma string, em formato de lista
# re.sub(padrão, novo_texto, texto) substitui todas as ocorrencias de um padrão por um novo texto

# Quantificadores(quantos?):

# * | zero ou mais vezes | a, aa, aaa, vazio
# + | uma ou mais vezes | a, aa, aaaa , não vazio
# ? | zero ou uma vez | a, vazio
# {n} | exatamente n vezes | a{3} só pega aaa
# {n,m} | minimo n e maximo m vezes | a{q,4} pega aa, aaa, aaaa

# Classes de caractere(o que ?):

# .  | qualquer caractere exeto nova linha |  OPOSTO:  - 
# \d | qualquer digito 0 - 9|  OPOSTO: \D não digito
# \w | qualquer caractere de palavra a-z, A-Z, 0-9 | OPOSTO: \W não palavra
# \s | qualquer espaço em branco (spaço, tabulação, nova linha | OPOSTO: \S não espaço
# [] | um dos caracteres dentro dos colchetes | OPOSTO: [^ ] nenhum dos caracteres

# Ancoras(onde?):

# ^ | inicio da string
# $ | fim da string
# \b | limite da palavra (inicio ou fim de uma palavra)


# ex: 

# texto = "Nossos códigos são: A-123, B-45, C-987. O código X-000 é antigo."

# codigo_padro = r"[A-Z]-\d{3}"

# retorno = re.findall(codigo_padro, texto)

# print(f"Filtragem {retorno}")

# primeiro_na_filtragem = re.search(codigo_padro, texto)

# if primeiro_na_filtragem:
#     print(f"Primeiro codigo: {primeiro_na_filtragem.group()}")
#1) Extração de e-mails: Utilizar expressões regulares para extrair e-mails válidos de um texto de 
# exemplo e armazená-los em uma lista.

# Texto de Exemplo:

# artigo = "Entre em contato conosco em suporte@minhaempresa.com.br ou
# vendas@minhaempresa.org. Você pode me encontrar em
# meu.email@pessoal.com. Ou, se preferir, use um-email_invalido@.com
# ou somente texto sem email."

# Saída Esperada:

# ['suporte@minhaempresa.com.br', 'vendas@minhaempresa.org',
# 'meu.email@pessoal.com']

    # codigo:

# import re

# artigo = """Entre em contato conosco em suporte@minhaempresa.com.br ou
# vendas@minhaempresa.org. Você pode me encontrar em
# meu.email@pessoal.com. Ou, se preferir, use um-email_invalido@.com
# ou somente texto sem email."""

# filtro= r'[\w\.-]+@[\w\.-]+\.[\w]{2,4}'

# email_filtros= re.findall(filtro,artigo)

# print(email_filtros)

# -------------------------------------------------------------------------------------


# 2) Crie uma função que valide se uma string corresponde ao formato de placa de
# carro brasileira antiga (3 letras, 4 números) ou nova (3 letras, 1 número, 1 letra,
# 2 números). A função deve retornar True se a placa for válida e False caso
# contrário.

# Exemplos de Teste:

# ● "ABC1234" -> True (formato antigo)
# ● "XYZ9A87" -> True (formato novo)
# ● "ABC123" -> False
# ● "1234ABC" -> False
# ● "ABCD1234" -> False

    # codigo:

import re

# def validação_de_placa(placa):
    
#     antiga = r'^[A-Z]{3}\d{4}$'
#     nova = r'^[A-Z]{3}\d{1}[A-Z]{1}\d{2}$'

#     valido1=re.findall(antiga,placa)
#     valido2=re.findall(nova,placa)

#     return bool(valido1 or valido2)

# placa=input("\nDigite sua placa:")

# a=validação_de_placa(placa)

# print(a)

# -------------------------------------------------------------------------------------

# 3)Divisão de parágrafos em sentenças: Dividir um parágrafo em uma lista de sentenças, considerando 
# pontos, interrogações e exclamações como terminadores de sentença, ignorando espaços extras.

# Parágrafo de Exemplo:

# paragrafo = """Olá! Como você está? Espero que esteja tudo bem. Este é
# um exemplo de parágrafo. Fim."""

# Saída Esperada:

# ['Olá', 'Como você está', 'Espero que esteja tudo bem', 'Este é um
# exemplo de parágrafo', 'Fim']

    # codigo:

# import re

# paragrafo = """Olá! Como você está? Espero que esteja tudo bem. Este é
# um exemplo de parágrafo. Fim."""

# filtro = r'\s*(.*?)[!?.]'

# filtragem=re.findall(filtro, paragrafo)

# print(filtragem)

# -------------------------------------------------------------------------------------


# 4)Extração de hashtags de tweets: Extrair todas as hashtags (palavras que começam com #) de uma
# string que representa um tweet.

# Tweet de Exemplo:

# tweet = "Adorei a aula de #Python hoje! #Programacao #DataScience
# com #Regex_poderoso. Sem hashtag aqui."

# Saída Esperada:

# ['#Python', '#Programacao', '#DataScience', '#Regex_poderoso']

    # codigo:

# import re

# tweet ="""Adorei a aula de #Python hoje! #Programacao #DataScience
# com #Regex_poderoso. Sem hashtag aqui."""

# filtro = r'[#]\w+'

# filtragem= re.findall( filtro, tweet)

# print(filtragem)

# -------------------------------------------------------------------------------------

# 5)Limpeza de strings com ruídos: Limpar uma string com caracteres especiais e múltiplos espaços, 
# resultando em uma string contendo apenas letras, números e espaços simples.

# String de Exemplo:

# dados_sujos = " Olá, Mundo! #@$123 Isso é um teste. Com muitos
# espaços!! "

# Saída Esperada:

# "Olá Mundo 123 Isso é um teste Com muitos espaços"

    # codigo:

# import re

# dados_sujos = """ Olá, Mundo! #@$123 Isso é um teste. Com muitos
# espaços!! """


# filtragem=re.sub(r'[^\w\s]', ' ', dados_sujos)
# filtragem_de_espacos=re.sub(r'\s+', ' ', filtragem).strip()

# print(filtragem_de_espacos)
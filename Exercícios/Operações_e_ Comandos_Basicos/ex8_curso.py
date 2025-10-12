# 1) Analise o código abaixo com atenção. Sem executá-lo, preveja exatamente o
#    que será impresso no final. Justifique sua resposta explicando o que acontece
#    com a variável número e com a lista_dados dentro e fora da função.

# Resposta: 

#   primeiro print: Fira da função (antes): numero = 10 lista_dado = [1, 2, 3]

#   segundo print: -> Dentro da função (antes): x=10 , y= [1 ,2 ,3]

#   terceiro print: -> Dentro da função (depois): x = 100, y = [1, 2, 3, 99]

#   Obs: Na questõa não da para entender se quer saber os valores que ficariam após a 
#        função ou se realmente quer verificar o print, então estou informando as duas versões: 
 
#   quarto print (print real): Fora da função (depois): numero = ???, lista_dado = ???

#   quarto print (valores): Fora da função (depois): numero = 10, lista_dado = [1,2,3,99]

#   justificativa: A variavel do tipo int, não é modificada pois é modificado na função e não retorna e armazena esse valor alterado, 
#                já a lista modifica, porque utiliza uma função para inserir um valor dentro da lista e não para subistituir a lista.


# ---------------------------------------------------------------------------

# 2) Crie uma função chamada calcular_imc que receba dois argumentos: peso (em
#    kg) e altura (em metros). A função deve calcular e retornar o valor do IMC. A
#    fórmula é: IMC = peso / (altura * altura). Crie uma segunda função para realizar a
#    classificação do IMC segundo a tabela:

# Codigo:

# def calcular_imc(peso, altura):

#     return peso / (altura * altura)

# def classificacao(imc):

#     if imc < 18.5:
#         print("\nAbaixo do peso normal")
#     elif imc >=18.9 and imc <=24.9:
#         print("\nPeso normal")
#     elif imc >=25.0 and imc <=29.9:
#         print("\nExcesso de peso")
#     elif imc >=30.0 and imc <=34.9:
#         print("\nObesidade classe I")
#     elif imc >=35.0 and imc <=39.9:
#         print("\nObesidade classe II")
#     else:
#         print("\nObesidade classe III")
#     return

# peso = float(input("\nInsita o seu peso em Kg: "))
# altura = float(input("\nInsira a sua altura em Metros: "))

# imc = calcular_imc(peso,altura)

# classificacao(imc)

# ---------------------------------------------------------------------------


# 3) Escreva uma função chamada saudar que receba um nome e uma saudacao
#    opcional. Se a saudação não for fornecida, ela deve usar "Olá" como padrão. A
#    função deve retornar uma string formatada.

# Codigo:

# def saudar(nome):
    
#     if nome == "":
#         return "\nOlá, seja bem-vindo !"

#     else:
#         return f"\nOlá {nome}, seja bem-vindo !"

# nome = input("\nInforme seu nome: ")

# print(saudar(nome))


# ---------------------------------------------------------------------------

# 4) Crie uma função chamada analisar_notas que receba uma lista de notas. A
#    função deve retornar três valores: a maior nota, a menor nota e a média das
#    notas

# Codigo:

# def analisar_notas(notas):

#     maior= max(notas)
#     menor= min(notas)
#     media= sum(notas) / len(notas)

#     return maior, menor, media
    
# lista_de_notas=[10, 5, 8]

# maior_nota, menor_nota, media_nota = analisar_notas(lista_de_notas)

# print(f"Maior nota: {maior_nota:.2f}")
# print(f"Menor nota: {menor_nota:.2f}")
# print(f"Media das notas: {media_nota:.2f}")

# ---------------------------------------------------------------------------

# 5) Escreva uma função chamada somar_tudo que possa receber um número
#    variável de argumentos numéricos e retorne a soma de todos eles.

# Codigo:

# def somar_tudo(*numeros):
#     return sum(numeros)

# print(f"A soma de 1, 4 , 5 e 7: '{somar_tudo(1,4,5,7)}'")
# print(f"A soma de 2, 4, 40 e 10: '{somar_tudo(2,4,40,10)}'")
# print(f"A soma de 66, 42, 6 e 9: '{somar_tudo(66,42,6,9)}'")


# ---------------------------------------------------------------------------

# 6) Crie uma função chamada gerar_relatorio que receba um número variável
#    de argumentos nomeados (keyword arguments) e imprima um relatório
#    formatado com cada par chave-valor. 
# 
#    Ex: gerar_relatorio(nome="João
#    Silva", idade=30, cidade="São Paulo", profissao="Engenheiro")
#    e retornaria:
# 
#    Nome: João Silva
#    Idade: 30
#    Cidade: São Paulo
#    Profissao: Engenheiro


# Codigo:

# def gerar_relatorio(**kwargs):

#     for chave, valor in kwargs.items():
#         print(f"{chave} : {valor}")

# gerar_relatorio(nome = "Neto", idade = 18, profissao = "estudante", cidade= "aracaju")

# ---------------------------------------------------------------------------

# 7) Crie uma função processar_pedido que receba o nome de um cliente como
#    primeiro argumento, seguido por uma lista variável de itens do pedido (*args), e
#    por fim, detalhes adicionais como argumentos nomeados (**kwargs, ex:
#    pagamento="cartão", entrega="urgente"). A função deve imprimir um resumo do
#    pedido.


# Codigo:

# def processar_pedido( nome, *itens, **detalhes_pedido):

#     print(f"\nNome do cliente: {nome}")
#     print("-"*30)

#     for iterador, item in enumerate(itens, start=1):
        
#         print(f" item {iterador} = {item}")

#     print("-"*30)

#     for chave, valor in detalhes_pedido.items():
#         print(f" {chave} : {valor}")

#     print("-"*30)

# nome="iderval"
# itens=["pão","queijo", "manteira", "cebola","tomate", "requeijão"]
# detalhes={"Pagamento":"Cartão", "Entrega": "urgente" }

# processar_pedido(nome,*itens,**detalhes)


# ---------------------------------------------------------------------------

# 8) Você tem uma lista de produtos, onde cada produto é um dicionário. Crie uma
#    função filtrar_produtos que recebe a lista de produtos e um preco_maximo. A
#    função deve retornar uma nova lista contendo apenas os produtos cujo preço é
#    menor ou igual ao preco_maximo.


# Codigo:

# def filtrar_produtos(preco_max,*lista):

#     lista_filtragem=[]

#     for produto in lista:
#         for chave, valor in produto.items():
#             if valor <= preco_max:
#                 lista_filtragem.append({chave : valor})

#     return lista_filtragem

# lista_de_produtos=[{"Arroz": 4.50},{"Macarrão": 3.00},{"Babana": 12.00},{"Abacaxi": 7.00},{"Mateiga": 5.00},{"Pão": 1.00},]
# preco_max=float(input("\nDigite maximo para filtrar os produtos: "))

# preco_filtrado=filtrar_produtos(preco_max,*lista_de_produtos)

# for item in preco_filtrado:
#     for chave, valor in  item.items():
#         print(f"Item: {chave} tem o valor: {valor}")

# ---------------------------------------------------------------------------

# 9) Crie uma função criar_perfil_usuario que aceite dois argumentos obrigatórios
#    (nome e email) e uma quantidade variável de informações adicionais usando
#    argumentos nomeados (**kwargs). A função deve montar e retornar um
#    dicionário contendo todas as informações do perfil do usuário


# Codigo:

# def criar_perfil_usuario(nome,email,**informacoes):
    
#     perfil={}
#     perfil["nome"]=nome
#     perfil["email"]=email
    
#     perfil.update(informacoes)

#     return perfil


# informacoes={}

# nome=input("\nInsira seu nome: ").strip()
# email=input("insira seu e-mail: ").strip()
# informacoes["idade"]=input("insira sua idade: ").strip()
# informacoes["cpf"]=input("insira seu cpf: ").strip()

# perfil=criar_perfil_usuario(nome, email, **informacoes)

# print(perfil)
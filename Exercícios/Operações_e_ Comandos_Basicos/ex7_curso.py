# 1) Lista de Tarefas (To-Do List): Você está criando um aplicativo simples de
#    lista de tarefas. Um usuário precisa armazenar suas tarefas do dia. Ele deve ser
#    capaz de adicionar novas tarefas, marcar tarefas como concluídas (removê-las) e ver
#    as tarefas na ordem em que foram adicionadas.
 
# Resposta: Conjunto, pois dict aceita o mesmo valor já existente o que não aceita é a chave, e as outras estruturas aceitam valores repetidos.



# --------------------------------------------------------------------------------------------------------------------


# 2) Cenário 2: Coordenadas RGB de uma Cor: Em um software de design gráfico, você
#    precisa representar uma cor específica, como o vermelho puro da Google, que é
#    composto pelos valores (234, 67, 53). Esses três valores (Vermelho, Verde, Azul)
#    sempre andam juntos, em uma ordem fixa, e nunca devem ser alterados
#    individualmente para não corromper a representação da cor.

# Resposta: Tupla, pois não poderá ser alterada, e garante a ordenação fixa da seguencia do codigo inserina na crianção dela.


# --------------------------------------------------------------------------------------------------------------------


# 3) Cenário 3: Inscrições em um Sorteio: Você está organizando um sorteio online. As
    #  pessoas se inscrevem fornecendo seu número de CPF. Para garantir que o sorteio
    #  seja justo, cada pessoa só pode se inscrever uma única vez. A ordem de inscrição
    #  não importa, mas você precisa de uma forma muito rápida de verificar se um CPF já
    #  foi cadastrado para evitar duplicatas.

# Resposta: Conjunto, pois garante que só ira existir um unico cpf, e pode ser verificado se o cpf esta dentro utilizando o "in"

# --------------------------------------------------------------------------------------------------------------------

# 4) Cenário 4: Cadastro de Clientes: Você está desenvolvendo um sistema para uma loja.
#    Para cada cliente, você precisa armazenar várias informações: nome, e-mail e
#    telefone. Você precisa ser capaz de buscar rapidamente todas as informações de um
#    cliente usando seu e-mail como identificador único.

# Resposta: dict pois ele é uma estrutura com chave e valor, e pode ser facilmente acessada chamando a chave e-mail do determinado cliente.

# --------------------------------------------------------------------------------------------------------------------

# 5)  Cenário 5: Permissões de Usuário em um Sistema: Em um sistema complexo, cada
#     usuário pode ter um conjunto de permissões (ex: 'admin', 'editor', 'visualizador').
#     Essas permissões são fixas e definidas no momento da criação do perfil do usuário e
#     não devem ser alteradas durante a sessão. O sistema precisa verificar rapidamente
#     se um usuário possui uma determinada permissão.

# Resposta: tupla, pois é imutavel então "fixas", e podem ser acessadas.

# --------------------------------------------------------------------------------------------------------------------


# 6) Você precisa criar um sistema simples para armazenar informações sobre produtos
#    de uma loja. Cada produto tem um código único (ID) e um nome. Seu programa deve
#    armazenar três produtos e, em seguida, permitir que o usuário digite um ID para buscar
#    e imprimir o nome do produto correspondente.

#    Dados de Entrada:

#        ● Produto 1: ID 101, Nome Camiseta
#        ● Produto 2: ID 102, Nome Calça Jeans
#        ● Produto 3: ID 103, Nome Tênis

# Codigo: 

produtos={}
id_contador=100

for iterador in range(3):

    nome_produto= input("\nDigite o nome do produto: ")

    id_contador+=1
    produtos[id_contador] = nome_produto

consulta=int(input("\nDigite o id do produto: "))

if consulta in produtos:
    print(produtos[consulta])
else:
    print("\nProduto não existe, ou id incorreto")


# --------------------------------------------------------------------------------------------------------------------

# 7) Você recebeu uma frase e sua tarefa é contar a frequência de cada palavra. Para
#    simplificar, desconsidere maiúsculas/minúsculas (ou seja, "Python" e "python" devem
#    ser contadas como a mesma palavra). O resultado final deve mostrar cada palavra única
#    e o número de vezes que ela apareceu.

# Codigo: 

palavras_contadas={}

frase = "O Python é uma Linguagem de Programação Poderosa e Versátil pois o Python é Simples de Aprender"
frase = frase.lower().split()

for palavra in frase:
    if palavra in palavras_contadas:
        palavras_contadas[palavra] += 1
    else:
        palavras_contadas[palavra] = 1
        
print(palavras_contadas)




# --------------------------------------------------------------------------------------------------------------------

# 8) Você recebeu uma lista de e-mails de participantes de um evento, mas a lista contém
#    vários e-mails duplicados. Sua tarefa é criar uma nova coleção que contenha apenas os
#    e-mails únicos e, em seguida, imprimir a quantidade de participantes únicos.

#    Dados de Entrada:

#       emails_participantes = [ 'ana@email.com', 'bruno@email.com', 'carla@email.com', "daniel@email.com", 'ana@email.com', 'bruno@email.com', 'emilia@email.com']

# Codigo: 

    
emails_participantes = [ 'ana@email.com', 'bruno@email.com', 'carla@email.com', "daniel@email.com", 'ana@email.com', 'bruno@email.com', 'emilia@email.com']

participantes_unicos = set( emails_participantes)

print(f"\nQuantidade de participantes unicos: {len(participantes_unicos)}")

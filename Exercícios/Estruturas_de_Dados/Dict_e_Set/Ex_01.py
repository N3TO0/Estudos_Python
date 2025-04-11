#Anotações sobre dict

#obt={}


#   Chave      valor
#obt['nome'] = 'Neto' #cria uma chave citada com o valor citado
#obt['sobre_nome'] = 'Show' #cria uma chave citada com o valor citado 
#obt['nome'] = 'Iderval' #O valor muda da chave citada
#del obt['sobre_nome'] #deleta a chave e o valor da chave citada

#print('\n',obt) #retorna o dicionario, com as chaves e valores contido dentro 

#--------------------------------------------------------

#obs =  { 'nome': 'iderval' , 'sobrenome' : 'neto'}


#Verifica se contem uma chave com esse nome, e se tem um valor, caso tenha retorna o valor, caso não tenha retorna "None"       
#print(obs.get('sobrenome',None))

#--------------------------------------------------------

#obs={  'nome':'iderval', 'sobrenome': 'neto', 'idade': 19, }


#pesquisa o valor pela chave
#print(obs['nome'])

#pesquisa pela chave e caso não exista essa chave, retorna a msg que citou depois da chave pesquisada
#print(obs.get('idade', 'não contem'))

#Verifica quantas chaves contem no dicionario
#print(len(obs))

#Retorna apenas as chaves
#print(obs.keys())

#Retorna apenas os valores
#print(obs.values())

#Retorna a chave e o valor 
#print(obs.items())

#Repete a quantidade de itens, e retorna a chave e o valor
#a=0
#for chave, valor in obs.items():
#    a+=1
#    print(f'{a} - ',chave,':',valor)

#Pesquisa se contem a chave, e caso não tenha, é criado uma chave com o valor, e caso exista não faz nada com a chave existente.
#obs.setdefault('carro_cor', 'vermelho')
#print(obs['carro_cor'])

#dicionario = {'carro': 'gol', 'cor':'azul', 'tamanho': 'grande', 'l1': [1,2,3,4] }

#COPIA E CASO ALTERE ESSE DICIONARIO, NÃO IRA ALTERAR NO ORIGINAL A MENSO QUE SEJA VALOR MUTAVEL, MAS CASO RETIRE A COPY(), IRA MUDAR NO ORIGINAL TBM.
#dicionario2 = dicionario.copy()
#dicionario2['carro'] = 'sla'
#print(dicionario)

#Caso queria um que não altere listas tbm, ussase 'import copy' e usasse deepcopy()
#import copy
#dicionario2 = copy.deepcopy(dicionario)
#dicionario2['l1'][0] = 2023
#print(dicionario2)
#print(dicionario)


#apaga um item com a chave citada
#dicionario.pop('carro')
#print(dicionario)

#apaga a o ultimo item do dicionario
#apaga um item com a chave citada
#dicionario.popitem()
#print(dicionario)

#atualiza o valor citando os items, e cria tabém
#dicionario.update({'carro': 'sla'})
#print(dicionario)














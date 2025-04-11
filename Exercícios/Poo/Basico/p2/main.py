from classes2 import Clientes


#Criando o bjeto pessoa1
pessoa1=Clientes('Neto','idervaljose80@gmail.com','Platinum')
#Mudando de plano
pessoa1.novo_plano('Basic')
#Retornando plano atual
print('\n',pessoa1.plano)

pessoa1.filmes('Uma dia', 'Platinum')
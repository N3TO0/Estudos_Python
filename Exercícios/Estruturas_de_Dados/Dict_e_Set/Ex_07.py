#args kwargs

#args, é para ser usado em lista
#kwargs é apra ser usado em dicionario

#args recebe valores não nomeados ex (1,2,3,'neto)
#kwargs recebe valores nomeados ex ('nome':'neto')

#exemplo com função:
#def mostro_argumentos_nomeados(*args,**kwargs):
#    for chave, valor in kwargs.items():
#        print(chave,': ',valor)
#    return 

#mostro_argumentos_nomeados(1,2,3,4,'Neto','Joana', nome1='tobias', nome2='clear')
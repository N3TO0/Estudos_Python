dicionario1={'Nome1':'Neto','Sobre_Nome1':'Souza'}
dicionario2={'Nome2':'Tadeu','Sobre_Nome2':'Lima'}

dic={**dicionario2,**dicionario1}

#for chave, valor in dic.items():
#    print( valor)
    
def uou(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)
    return
uou(**dic)    


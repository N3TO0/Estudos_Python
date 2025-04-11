#Set é uma estrutura de dados como list, tuple e dict

#Set não recebe o valor em rodem, é aleatorio
#Quaquer valor duplicado quer o set receber, será juntado, apenas tendo um valor daquele
# ex:
#   

#s1={'luiz',2,'luiz',3,5,2}
#print(s1, type(s1))

#Normalemente usado para apagar valores repetidos ex:

#a=[1,2,3,4,5,4,3,2,1,1,1,2,2,3,3,'iderval']
#a=set(a)
#a=list(a)
#print(a)
#a=set(a)

#Acrescenta o valor entre o parentase no set
#a.add(1)

#Update ura acrescentar a lista de forma iteravel ou seja cada caractere da str ira ser separado e colocado.
#a.update(('iderval',1,1,1,2,3,4,5,6,7,8,10))
#a=list(a)
#print(a)

#Esse comando limpa o set
#a.clear()
#print(a)

#Esse comando discarta o elemento que vc escolheu
#a.discard('iderval')
#print(a)

#Operadores para set

#s1={'1','5','6','10',}
#s2={'6','7','2','5',}

#Uni as duas set
#s3= s1 | s2

#Retorna os valores que contem em comum
#s3= s1 & s2

#Retorna os valores que não tem em comum apenas do set a esquerda
#s3= s1 - s2

#Retorna os valores não contem em comum de ambos 
#s3= s1 ^ s2

#print(s3)


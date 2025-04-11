#Mapeamento list comprehension 

#lista=[numero for numero in range(10)]
#print(lista)

#lista2=[ numero * 2 for numero in range(10)]
#print(lista2)

#produtos=[{'nome':'p1','peço':10},{'nome':'p2','peço':20},{'nome':'p3','peço':30}]

#alteração=[
#    {**produto, 'peço': produto['peço'] *10}
#    if produto['peço'] > 20 else{**produto}
#    for produto in produtos]

#print(*alteração, sep='\n')

#Filtro list comprehendion
#                             filtro
lista= [n for n in range(10) if n <= 5]
print(lista)

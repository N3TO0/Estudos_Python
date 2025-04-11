lista=["neto","Jonas","Darwin", 26, True]

lista.append("lula") #acrescentei a lista
a= lista.pop() #removi, e armazenei o valor que removi no a
lista.append(a) #acrescentei o valor da variavel a na lista  
del lista[1] #deletei o valor na posição 1 da lista, o "darwin"

print(lista,a) # retornei na tela a lista alterada e acrescentei a variavel a fora da lista 
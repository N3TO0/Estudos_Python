#Explicação sobre loop aninhado,(um loop dentro de outro loop)

#Util para quando necessitar percorrer estruturas de dados como listas dentro de listas, ou multiplas iterações em multiplos citerios.

#Para cada loop externo, o loop intterno completa todas suas iterações

#Exemplo iterar sobre uma lista de lista (Matriz)

#Exemplo, lista dentro de lista
#matriz=[
#    [1,2,3],
#    [4,5,6],
#    [7,8,9],
#    [10,11,12]
#]

#for linha in matriz:
#    for elemento in linha:
#        print(elemento, end=' ')
        
#Exemplo contar combinações

#for i in range(1,5):
#    for j in range(1,5):
#        print(i,j)

#Exemplo loop aninhado para modificar valores de um dicionario com listas
boletim={'matematica':[0,0,0,0],
         'ciencias':[0,0,0,0],
         'portugues':[0,0,0,0],
         'fisica':[0,0,0,0]
}

for materia, notas in boletim.items():
    print(f'\nMateria: {materia}')
    for nota in range(len(notas)):
        notas[nota]=int(input(f'\nNota({nota+1}): ').strip())
    Media=sum(notas)/4
    
    print(f'\nMédia: {Media:.1f}')
    



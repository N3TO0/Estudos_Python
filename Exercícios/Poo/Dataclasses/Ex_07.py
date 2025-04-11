#"Names tuple", criar classes de objetos que
#são agrupamento de atributos, como classes normais
#sem metodos, ou registro de base de dados.

from collections import namedtuple

#Classe com objeto de dois valores, no verso "valor" 
#e "naipe"
Carta = namedtuple('carta',['valor','naipe']) 
as_espadas = Carta('A','Espadas')

print(as_espadas)
print(as_espadas.naipe)
print(as_espadas.valor)
 
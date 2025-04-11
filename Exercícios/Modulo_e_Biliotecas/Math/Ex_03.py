#CODIGO PARA SORTEAR NOME UTILIZANDO BLIBLIOTECA.

import math
import random
a=str(input("\nDigite o nome do aluno 1: "))
b=str(input("\nDigite o nome do aluno 2: "))
c=str(input("\nDigite o nome do aluno 3: "))
d=str(input("\nDigite o nome do aluno 4: "))

x=[ a, b, c, d ]

z= random.choice(x) 

print("\nO aluno sorteado foi: {}".format(z))
#CODIGO PARA ESCOLHER UMA ORDEM.

import random

a1=str(input("\nDigite o nome do aluno 1: "))
a2=str(input("\nDigite o nome do aluno 2: "))
a3=str(input("\nDigite o nome do aluno 3: "))
a4=str(input("\nDigite o nome do aluno 4: "))

l=[a1,a2,a3,a4]

r=random.shuffle(l)

print("\nA ordem fica:")

for a in l:
 
 print(a)

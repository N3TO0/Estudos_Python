#CODIGO QUE INSERE NUMERO INICIAL E LIMITE E INFORMA QUAIS NUMEROS PARES ESTÃO ENTRE ELES.
from time import sleep

print("\n{:=^50}".format(" Numeros Pares "))

print("\nEste programa ira informar quais numeros pares contem\ndo numero inicial até o numero limite, por favor informe:")

a=int(input("\nNumero Inicial: ").strip())
d=int(input("Numero Limite: ").strip())


for c in range ( a, d):
    if c % 2 == 0:
        print("{}".format(c))

#OU

#if a % 2 == 0: #par
#    for c in range (a,d, 2):
#        print("\nNumero {} é par".format(c))
#else:
 #   b=a+1
 #   for b in range(b, d ,2):
 #       print("\nNumero {} é par".format(b))
 
#print("\n{:=^50}\n".format(" Fim "))

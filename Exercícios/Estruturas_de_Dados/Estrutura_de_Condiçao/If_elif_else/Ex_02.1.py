#CODIGO PARA CALCULAR A MEDIA E SE PASSOU.

import math

print("\n{:=^50}".format(" Resultado Da Média "))

a=float(input("\nNota 1: ").strip())
b=float(input("Nota 2: ").strip())
c=(a+b)/2

if c>=9:
    print("\nMédia: {} \n\nMédia exelente".format(math.floor(c)))
elif c>=7:
    print("\nMédia: {} \n\nMédia Boa".format(math.floor(c)))
elif c>=5:
    print("\nMédia: {} \n\nMédia Mediana".format(math.floor(c)))
else:
    print("\nMédia: {} \n\nMédia Insatisfatoria".format(math.floor(c)))

print("\n{:=^50}".format(" Fim "))
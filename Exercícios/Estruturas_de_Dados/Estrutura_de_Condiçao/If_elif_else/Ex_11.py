#CODIGO QUE INFORMA SE OS VALORES RECEBIDOS SÃO IGUAIS OU QUAL É O MAIRO E O MENOR.
from time import sleep

print("\n{:=^50}".format(" Maior, Menor ou Igual "))

print("\nDigite dois valores e saiba qual é o maior, \nmenor ou se são iguais!")

a=int(input("\nDigite o valor 1: ").strip())
b=int(input("\nDigite o valor 2: ").strip())

if a>b:
    print("\nVarificando...")
    sleep(1)
    print("\n{} é o numero menor e {} é o maior!".format(b,a))
elif a<b:
    print("\nVerificando...")
    sleep(1)
    print("\n{} é o numero menor e {} é o maior!".format(a,b))
else:
    print("\nVerificando...")
    sleep(1)
    print("\nOs numero {} e {} tem o mesmo valor!!".format(a,b))


print("\n{:=^50}".format(" Fim ")) 
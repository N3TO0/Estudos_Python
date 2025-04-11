#CODIGO QUE INSERE NUMERO INICIAL E NUMERO LIMITE E INFORMA OS NUMEROS QUE SÃO DIVISIVEIS POR 3.

print("\n{:=^50}".format(" Numeros Impares Multipos De 3 "))
 
print("\nInforme o numero inicial e o numero limite,\npara saber quais são divisiveis por 3!")

b=int(input("\nNumero Inicial: ").strip())
d=int(input("Numero Limite: ").strip())

for a in range (b, d):
    if a % 3 == 0:
        print("\n{}".format(a))

print("{:=^50}".format(" Fim"))
#CODIGO QUER INFORMA O PREÇO DA PASSAGEM DE ACORDO COM O KM QUE IRA PERCORRER.

print("\n{:=^50}".format(" Precificação de Passagem "))

b=float(input("\nInforme a distancia que deseja viajar em km: ").strip())

if b>200:
    c=b*0.45
    print("\nO valor da passagem é {:.2f}".format(c))
else:
    g=b*0.55
    print("\nO valor da passagem é {:.2f}".format(g))

print("\n{:=^50}".format(" Fim "))
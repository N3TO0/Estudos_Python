#CODIGO PARA CALCULAR AUMENTO SALARIAL

print("{:=^50}".format(" Calculo de Aumento Salarial "))

a=float(input("\nQual é o valor do seu salário ? :  ").strip())
#b=float(input("\nQual a porcentagem do aumento ? : ").strip())

if a > 1250:
    print("\nSalario total: R$ {:.2f}".format((a*10)/100+a))
else:
    print("\nSalario total: R$ {:.2f}".format((a*15)/100+a))

print("{:=^50}".format(" Fim "))
#CODIO PARA CALCULAR O VALOR DO AUMENTO BASEADO EM PORSENTAGEM.

a=float(input("\nDigite o valor do seu salario:"))
b=float(input("\nDigite a porcentagem do aumento:"))
c=(a*b)/100

print("\nValor do novo salario: {:.2f} R$".format(c+a))
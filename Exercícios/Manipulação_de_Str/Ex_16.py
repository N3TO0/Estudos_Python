#CODIGO QUER RECEBE UM VALOR E INFORMA QUAIS SÃO A UNIDADE, DEZENA, CENTENA, E MILHAR

num=str(input("\nDigite um numero de 0 a 9999: "))

num2=num.split()

num3=" ".join(num2)
 
print("\nUnidade: ", num3[3])
print("\nDezena: ",num3[2])
print("\nCentena: ",num3[1])
print("\nMilhar : ", num3[0],"\n")
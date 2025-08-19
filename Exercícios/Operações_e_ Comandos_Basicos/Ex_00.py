# CODIGO PARA RETORNAR UMA FRASE.

# nome = input("\nDigite um nome: ")
# n1 = int(input("\nDigite a primera nota: "))
# n2 = int(input("\nDigite a sunda nota: "))

# media = ((n1+n2) / 2)

# if media < 7:
#     resultado = "RREPROVADO"
# elif media >= 7:
#     resultado = "APROVADO" 

# print(f"\n\n{nome} foi {resultado} com Média: {media}\n")


#---------------------------------------------------------

# n1 = int(input("\ndigite o comprimento da primeira ponta: "))
# n2 = int(input("\ndigite o comprimento da segunda ponta: "))
# n3 = int(input("\ndigite o comprimento da terceira ponta: "))

# triangulo_perfeito = n1 == n2 == n3

# if triangulo_perfeito:
#     print("\n\nÉ um Triangulo Equilátero!!\n")
# else:
#     print("\n\nNão é um Triangulo Equilátero!!\n")

#---------------------------------------------------------

# n1=int(input("\nDigite o comprimeiro do primeiro lado:"))
# n2=int(input("\nDigite o comprimeiro do segundo lado:"))
# n3=int(input("\nDigite o comprimeiro do terceiro lado:"))

# if (n1+n2) > n3 and (n3 +n2) > n1 and (n1 +n3) > n2:
#     print("\n\nÉ prossivel formar um triangulo\n")
# else :
#     print("\n\nNão é possivel formar um triangulo\n")

#---------------------------------------------------------
# while 1:
    
#     lado1= input("digite o primeiro lado do triangulo")
#     lado2= input("digite o segundo lado do triangulo")
#     lado3= input("digite o terceiro lado do triangulo")

#     if lado1 

# ---------------------------------------------------------

# base=int(input("digire a base do triangulo: "))
# altura=int(input("digite a altura do triangulo: "))

# print(f"A area do triangulo é: {(base*altura)/2}")

#----------------------------------------------------------

# segundos=int(input("Digite os segundo: "))
# minutos=int(0)
# horas=int(0)

# while segundos >= 60:
#     segundos= segundos - 60
#     minutos = minutos + 1

# while minutos >= 60:
#     minutos = minutos - 60
#     horas = horas + 1

# print(f"O calculo de horas, munituos, segundo é: {horas}:{minutos}:{segundos}")

#--------------------------------------------------------

# segundos = int(input("\nDigite os segundos: "))
# minutos = int(0)
# horas = int(0)
 
# horas = segundos // 3600
# segundos = segundos % 3600

# minutos = segundos // 60
# segundos = segundos % 60

# print(f"\n\nhoras: {horas} \nMinutos: {minutos} \nSegundos: {segundos} \n\n")

#---------------------------------------------------------

# CAPITAL = int(input("\nDigite quanto de capital deseja investir: "))
# TAXA_DE_JUROS = float(input("\nDigite qual a porcentagem do juros por dia: "))
# TEMPO_DE_JUROS = int(input("\nDigite quantos dias deseja receber de volta: "))

# print(f"\n\nO valor que irá receber é: R$ {((( TAXA_DE_JUROS / CAPITAL ) * 100 ) * TEMPO_DE_JUROS ) + CAPITAL }\n\n")

#---------------------------------------------------------

# ENTRADA=int(input("\nDigite um numero para saber se é par ou impár e se esse numero é maior ou menor que 15\n\nNumero: "))


# if ENTRADA < 15 :
#     print(f"\n'{ENTRADA}' É menor que 15!!")
# elif ENTRADA == 15:
#     print(f"'{ENTRADA}' É igual a 15")
# else:
#     print(f"\n'{ENTRADA}' é maior que 15!!")

# if ENTRADA % 2 == 0:
#     print(f"\n\n'{ENTRADA}' é um numero par\n")
# else:
#     print(f"\n\n'{ENTRADA}' é um numerO impár\n")

#---------------------------------------------------------

# LAD1=int("Digite o comprimento do primeiro lado: ")
# LAD2=int("Digite o comprimento do segundo lado: ")
# LAD3=int("Digite o comprimento do terceiro lado: ")

# if (LAD1 == LAD2 or LAD2 == LAD3 or LAD1 == LAD3) and ( (LAD1 + LAD2) > LAD3 or (LAD3+ LAD1) > LAD2 or (LAD3 + LAD2) > LAD1 ):
#     print("Esse é um triangulo isóceles!")
# else:
#     print("Não é um triangulo isóceles!!")

#----------------------------------------------------------

# velocidade_atua=float(input("\nDigite quantos km está o veiculo está: "))

# if velocidade_atua > 80:
#     print(f"\nO veiculo foi multado por estar acima do limite de velocidade‼️\n\nVelocidade: {velocidade_atua} Km\nValor da multa: R${(velocidade_atua-80)*15}\n")

# elif velocidade_atua == 80:
#     print("\nCuidado você esta no limite de velocidade‼️\n")

# else:
#     print("\nPagarabéns vc está dentro do limite de velocidade 🎉🎉\n\n")

#-------------------------------------------------------------- 


# entrada = int( input("\nDigite um numero: ") )

# if entrada > 10:
#     print(f"\n{entrada} é maior que 10\n")
# elif entrada == 10:
#     print(f"\n{entrada} é igual que 10\n")
# else:
#     print(f"\n{entrada} é menor que 10\n")

#-------------------------------------------------------------

# entrada_1=input("\n\nDigite um numero ou letra :")
# entrada_2=input("\nDigite um numero ou letra :")

# if entrada_1 > entrada_2:
#     print(f"\n{entrada_1} é maior que {entrada_2}\n")
# else :
#     print(f"\n{entrada_2} é menor que {entrada_1}\n")

#------------------------------------------------------------

# n1=int(input("\nDigite a primeira nota: "))
# n2=int(input("\nDigite a primeira nota: "))

# if (n1 + n2)/2 < 6:
#     print("Você foi reprovado")
# else:
#     print("Você passouuu!!!")

# ----------------------------------------------------------

# ano_atual=int(input("\nDigite o ano atual para saber se é bisexto: "))

# if ano_atual / 400 or ((ano_atual % 4 == 0) and ano_atual % 100 != 0):
#     print("\nÉ bisexto\n")
# else:
#     print("\nNão é bisexto\n")

#-----------------------------------------------------------
# from math import sqrt

# numero=int(input("\nDigite um numero para saber a raiz quadrada dele: "))

# if numero > 0:
#     print(f"\nA raiz quadrada de {numero} é {sqrt(numero):.2f}\n")
# else:
#     print(f"\nNão é possivel calcular a raiz quadrada de {numero}\n")

#-----------------------------------------------------------

# altura=float(input("\nInforme sua altura: "))
# sexo=int(input("\nQual seu sexo ? \n\n1 - Masculino\n2 - Feminino \n\nDigite: "))

# if sexo == 1:
#     print(f"\nseu pesso ideal é : {((72.7 * altura) - 58):.1f}\n")
# elif sexo == 2:
#     print(f"\nseu pesso ideal é : {((62.1 * altura) - 44.7):.1f}\n")
# else: 
#     print("\nDigitou algo errado 😑\n")
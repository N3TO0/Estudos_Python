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


# # ---------------------------------------------------------

# n1 = int(input("\ndigite o comprimento da primeira ponta: "))
# n2 = int(input("\ndigite o comprimento da segunda ponta: "))
# n3 = int(input("\ndigite o comprimento da terceira ponta: "))

# triangulo_perfeito = n1 == n2 == n3

# if triangulo_perfeito:
#     print("\n\nÉ um Triangulo Equilátero!!\n")
# else:
#     print("\n\nNão é um Triangulo Equilátero!!\n")

# # ---------------------------------------------------------

n1=int(input("\nDigite o comprimeiro do primeiro lado:"))
n2=int(input("\nDigite o comprimeiro do segundo lado:"))
n3=int(input("\nDigite o comprimeiro do terceiro lado:"))

if (n1+n2) > n3 and (n3 +n2) > n1 and (n1 +n3) > n2:
    print("\n\nÉ prossivel formar um triangulo\n")
else :
    print("\n\nNão é possivel formar um triangulo\n")

#---------------------------------------------------------






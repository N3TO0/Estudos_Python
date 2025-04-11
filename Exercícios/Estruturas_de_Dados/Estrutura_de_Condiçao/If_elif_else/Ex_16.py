#CODIGO QUE INFORMA DIFERENTES DADOS SOBRE O DADO COLETADO

print("-"*50)

a=(input("\nDigite seu nome: ").strip())
b=(input("Digite sua idade: ").strip())

c=len(a) #quantidade de caractere
d=a[c-1] #ultima letra
e=a[0] #primeira letra


if a and b:
   
    print("\nSeu nome é: {}".format(a))
    print("\nSeu nome invertido é: {} ".format(a[::-1]))
    print("\nSeu nome contem espaços: "," " in a)
    print("\nseu nome tem letra 'n' : ", "n" in a)
    print("\nPrimeira letra do seu nome é: {}".format(e))
    print("\nUltima letra do seu nome é: {}\n\n".format(d))
else:

    print("\nDesculpe, você deixou campos vazios!\n\n")

print("-"*50)
    
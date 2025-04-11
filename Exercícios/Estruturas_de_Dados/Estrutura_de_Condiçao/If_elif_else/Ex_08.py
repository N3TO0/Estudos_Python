#CODIGO QUE INFORMA O MAIOR E O MENOR INDEPENDENTE DA SEGUENCIA DIGITADA. 

print("{:=^50}".format(" Maior e Menor "))

a=int(input("\nDigite um numero: ").strip)
b=int(input("\nDigire um numero: ").strip)
c=int(input("\nDogite um numero: ").strip)

if a > c > b:
    print("\nMaior: {}\nMenor: {}".format(a,b))
elif c < b < a :
    print("\nMaior: {}\nMenor: {}".format(a,c))
elif b > c > a:
    print("\nMaior: {}\nMenor: {}".format(b,a))
elif c < a < b:
    print("\nMaior: {}\nMenor: {}".format(b,c))
elif c > b > a:
    print("\nMaior: {}\nMenor: {}".format(c,a))     
else:
    print("\nMaior: {}\nMenor: {}".format(c,b))

print("{:=^50}".format(" Fim "))
#CODIGO PARA SABER ADIÇÃO, SUBRITAÇÃO, MULTIPLICAÇÃO, DIVISÃO INTEIRO, DIVISÃO REAL, POTENCIA E RESTO DO NUMERO DIGITADO.

a=int(input("\nDigite um valor: "))
b=int(input("\nDigite um valor: "))
c=int(input("\nDigite um valor: "))

d=a+b+c   # Adição
e=a-b-c   # Subitração 
f=a*b*c   # Mutiplicação 
h=a/b/c   # Divisão Inteiro
i=a**b    # Potencia
j=a//b    # Divisão Real
k=a%b     # Resto

print("\nO valor {} somada por {} e por {} \nresulta no valor: {}\n".format(a,b,c,d))
print("O valor {} subtraido por {} e por {} \nresulta no valor: {}\n".format(a,b,c,e))
print("O valor {} multiplicado por {} epor {} \nresulta no valor: {}\n".format(a,b,c,f))
print("O valor {} dividido por {} e por {} \nresulta no valor: {}\n".format(a,b,c,h))
print("O valor {} elevado a {} \nresulta no valor: {}\n".format(a,b,i))
print("O valor {} dividido por {} \nresulta no valor: {}\n".format(a,b,j))
print("O resto da dividação entre {} e {} \nresulta no valor: {}\n".format(a,b,k))
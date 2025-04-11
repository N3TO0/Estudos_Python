#CODIGO QUE INFORMA O PRIMERO E ULTIMO NOME DE UMA PESSOA.

a=str(input("Digite seu nome: ")).strip
lista=a.split()
print("O primeiro nome é {}".format(lista[0]))
print("O ultimo nome é {}".format(lista[len(lista)-1]))
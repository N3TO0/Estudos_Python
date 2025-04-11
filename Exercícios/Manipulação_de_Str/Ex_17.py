#CODIGO QUE RECEBE O NOME DA CIDADE E INFORMA SE CONTEM A PALAVRA SANTO OU NÃO NO PRIMEIRO NOME.

a=str(input("\nDigite o nome da sua cidade: "))

b=a.split()

print("\nO nome da sua cidade contem o nome Santo?: ",'Santo' == b[0] , "\n")
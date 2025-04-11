#CODIGO QUE LE O NOME COMPLETO, INFORMA ELE TUDO EM MINUSCULO E MAIUSCULO E DIZ QUANTAS LETRAS CONTEM NA VARIAVEL SEM CONTAT OS ESPAÇOS E INFORMA 
#A QUANTIADE DE LETRAS APENAS NO PRIMEIRO NOME.

nome=str(input("\nDigite seu nome completo: "))

print("\nTransforamndo tudo em maiusculo ficaria: ", nome.upper())

print("\nTransforamndo tudo em minusculo ficaria: ", nome.lower())

fatiamento=nome.split()

juntando="".join(fatiamento)

print("\nAs letras ao todo sem considerar o espaço são: ", len(juntando))

print("\nA quantidade de letras no primeiro nome é: ", len(fatiamento[0]),"\n")

print("\n ---------------------------------- \n\n")



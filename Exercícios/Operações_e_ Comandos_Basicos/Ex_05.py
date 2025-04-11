#CODIGO PARA SABER O OS TIPOS DO VALOR DIGITADO.

n=input("Digite para saber mais informações sobre o que digitou:")

print("Qual tipo de variavel foi digitada:\n",type(n))

print("O que digitou é um numero ?\n",n.isnumeric())

print("O que digitou é uma letra ?\n",n.isalpha())

print("O que digitou é uma letra maiuscula ?\n",n.isupper())

print("O que digitou é um letra minuscula ?\n",n.islower())

print("O que digitou é um numero ou uma letra ?\n",n.isalnum())

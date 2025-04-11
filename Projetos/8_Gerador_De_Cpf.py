#GERADOR DE CPF

from random import randint
cpf_digito_9='' #str
multiplicador = 10 #int
resultado=0 #int
cpf_digito_10="" #str
c=0 #int

for i in range(0,9,1):
    cpf_digito_9+=str(randint(0,9))

for c in cpf_digito_9:

    resultado += int(c) * multiplicador
    multiplicador -= 1

resultado = (resultado * 10) % 11

if resultado >= 9:
    resultado = 0
else:
    resultado = resultado
    
cpf_digito_10 = cpf_digito_9 + str(resultado)

multiplicador = 11
resultado = 0

for c in cpf_digito_10:

    resultado += int(c) * multiplicador
    multiplicador -= 1

resultado = (resultado * 10) % 11


cpf_digito_11 = cpf_digito_10 + str(resultado)

print(f'\n\nCpf: {cpf_digito_11}')



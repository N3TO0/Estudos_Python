
valor_da_compra=input("\nDigite o valor total da compra: ")
FRETE = 15.00

desconto1=input("\nDigite o nome do primeiro cupom: ").lower()
desconto2=input("\nDigite o nome do segundo cupom: ").lower()

valor_desconto = 0.00
valor_desconto_frete = 0.00

valor_da_compra=float(valor_da_compra)

print(f"\n\nCompra: R$ {valor_da_compra:.2f}")
print(f"Frete: R$ {FRETE:.2f}")


if desconto1 == "desconto10" or desconto2 == "desconto10" :

    valor_desconto= (10 * valor_da_compra) / 100
    print(f"Cumpom 'esconto10' - R$ {valor_desconto:.2f}")

if desconto2 == "fretegratis0" or desconto2 == "fretegratis" :

    valor_desconto_frete = 15.00
    print(f"Cumpom 'fretegratis' - R$ {valor_desconto_frete:.2f}")

valor_total= valor_da_compra + FRETE - valor_desconto  - valor_desconto_frete

print(f"\nValor total: R$ {valor_total:.2f}\n\n")

# ---------------------------------------------------------------

senha_entrada=input("\nInforma a senha: ")

SENHA ="senha123"

if SENHA == senha_entrada:
    print("\nAcesso foi permitido\n\n")
else:
    print("\nAcesso foi Negado\n\n")

# ---------------------------------------------------------------

idade=int("\nInforme sua idade:")

if idade > 0 and idade <= 12:
    print("Você é Criança")
elif idade >= 13 and idade <= 17:
    print("Você é Adolescente")
elif idade > 18 <= 101:
    print("Você é Adulto")
else:
    print("Idade Não possivel!")

# obs: coloquei a idade limite 101 porque na minha cabeça ninguem vai passar disso ksksk.

# ---------------------------------------------------------------

dia= int(input("\nDigite um dos numeros de 1 a 7: "))

if dia == 1:
    print("\nSegunda\n")
elif dia == 2:
    print("\nTerça\n")
elif dia == 3:
    print("\nQuarta\n")
elif dia == 4:
    print("\nQuinta\n")
elif dia == 5:
    print("\nSexta\n")
elif dia == 6:
    print("\nSabado\n")
elif dia == 7:
    print("\nDomingo\n")
else:
    print("\nNumero não informado nas opções!\n")

# ---------------------------------------------------------------

idade=int(input("\nDigite sua idade: "))

tempo_de_trabalho=int(input("\nDigite quantos anos vc trabalhou: "))

if idade >= 65 or tempo_de_trabalho >= 30 or (idade >= 60 and tempo_de_trabalho >= 25):
    print("\nPode se aposentar!\n")
else:
    print("\nnão pode se aposentar!\n")

# ---------------------------------------------------------------

saque=int(input("\nDigite o valor que deseja sacar: "))

saque_imutavel = saque
n_cem=0
n_cinquenta=0
n_vinte=0
n_dez=0

while (saque>0):

    if saque >= 100:
        n_cem += 1
        saque -= 100

    elif saque >= 50:
        n_cinquenta += 1
        saque -= 50

    elif saque >= 20:
        n_vinte += 1
        saque -= 20

    elif saque >= 10:
        n_dez += 1
        saque -= 10
    

print(F"\nSaque de {saque_imutavel} em notas:\n\n{n_cem} de R$100\n{n_cinquenta} de R$50\n{n_vinte} de R$20\n{n_dez} de R$10\n")

# ----------------------------------------------------------------

altura=float(input("\nDigite sua altura: "))
peso=float(input("\nDigite seu peso: "))

imc= peso/(altura**2)

if  imc < 18.5:
    print("\nAbaixo do peso\n")

elif imc >=18.5 and imc < 24.9:
    print("\nPeso ideal\n")

elif imc >= 25.0  and imc <= 29.9:
    print("\nLevemente acima do peso\n")

elif imc >= 30.0 and imc < 34.9:
    print("\nObesidade grau I\n")
    
elif imc >= 35.0 and imc < 40.0:
    print("\nObesidade grau II (severa)\n")
else:
    print("\nObesidade grau III (mórbida)\n")


# ----------------------------------------------------------------

contador_sim=0


pergunta_1=input("\nTelefonou para a vítima no último mês?\nResposta: ").lower()

if pergunta_1 == "sim":
    contador_sim+=1

pergunta_2=input("\nEsteve no local do crime na última semana?\nResposta: ").lower()

if pergunta_2 == "sim":
    contador_sim+=1

pergunta_3=input("\nMora perto da vítima?\nResposta: ").lower()

if pergunta_3 == "sim":
    contador_sim+=1

pergunta_4=input("\nDevia para a vítima?\nResposta: ").lower()

if pergunta_4 == "sim":
    contador_sim+=1

pergunta_5=input("\nJá trabalhou com a vítima?\nResposta: ").lower()

if pergunta_5 == "sim":
    contador_sim+=1

if contador_sim == 2:
    print("\nVoce é um Suspeito!!")
elif contador_sim == 3 or contador_sim == 4:
    print("\nVoce é um Cúmplice!!")
elif contador_sim == 5:
    print("\nVoce é o Assassino!!")

else:
    print("\nVocê é Inocente!!")

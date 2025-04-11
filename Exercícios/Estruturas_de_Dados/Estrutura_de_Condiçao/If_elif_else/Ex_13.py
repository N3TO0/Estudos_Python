#CODIGO PARA CALCULAR O VALOR DO PRODUTO DEPENDENDO DE COMO VAI SER PAGO.

print("\n{:=^50}".format(" Calculando Valor "))

a=float(input("\nQual o valor do produto:R$ ").strip())
print("\nDigite o numero da opção quer deseja fazer o pagamento\n\n1 - Dinheiro ou Cheque.\n2 - Cartão de Debito.\n3 - Catão de Credito em até 2x.\n4 - Cartão  de Credito em até 3x ou mais.")
b=float(input("\nQual opção deseja ? : ").strip())

if b == 1 :
    c=a-(a*10)/100
    print("\nEssa opção contem 10% de desconto!!\nValor: R$ {:.2f}".format(c))
elif b == 2 :
    c=a-(a*5)/100
    print("\nEssa opção contem 5% de desconto!!\nValor: R$ {:.2f}".format(c))
elif b == 3 :
    c=a/2
    print("\nEssa opção não contem desconto!!\nValor parcelado em 2x: R$ {:.2f} ".format(c))
elif b == 4 :
    c=(a*20)/100+a
    print("\nEssa opção contem o acrescento de 20% de juros !!\nValor: R$ {:.2f}".format(c))
else:
    print("\nNão foi digitado nenhumas das opções informadas.")

print("\n{:=^50}".format(" Fim "))


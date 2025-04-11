#CODIGO PARA SABER VALOR DO REAL QUE OBTEM, EM DOLAR.

a=float(input("\nDigite o valor do dinheiro que tem: R$"))
# 1 dolar = 5,47 real
b=a/5.47

print("\n Você pode comprar: US${:.2f} Dólares".format(b))

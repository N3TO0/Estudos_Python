#CODIGO PARA SABER QUANTOS LITROS É NECESSARIO BASEADO EM METROS QUADRADOS.

a1=float(input("\nDigite a altura: "))
a2=float(input("\nDigite a largura: "))
a3=a1*a2
lm=2
a4=a3/lm

print("\nArea: {:.2f}\nTinta Necessaria:{:.2f}\n".format(a3, a4))
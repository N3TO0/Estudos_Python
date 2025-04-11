#CODIGO DE UM SISTEMA DE MULTA

a=" Sistema de Multas "
t=" Fim "
print("{:=^50}".format(a))

b=float(input("\nDigite quantos Km você estava: ").strip())
m=(b-80)*7

print("\nVocê ultrapassou o limite de velocidade!\nO valor da multa é de: R$ {:.2f}".format(m) if b>80 else"\nVocê esta dentro do limiete de velocidade, Parabéns!!\nTenha um bom dia!! Dirija com segurança!")

#if b > 80:
#    m=(b-80)*7
#    print("\nVocê ultrapassou o limite de velocidade!\nO valor da multa é de: R$ {:.2f} ".format(m))

#else:
#    print("\nVocê esta dentro do limiete de velocidade, Parabéns!!")

print("\n{:=^50}".format(t))
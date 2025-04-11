#CODIGO PARA CALCULAR O IMC DE UMA PESSOA.

print("\n{:=^50}".format(" Calculando IMC "))

print("\nPara calcular o Imc é preciso que me forneca algunsa dados,\nno caso a sua altura e peso!!")

a=float(input("\nAltura: M ").strip())
b=float(input("\nPeso: Kg ").strip())

c=b/(a**2)

if c < 18.5 :
    print("\nSeu Imc é de {:.2f},\nE está abaixo do peso!".format(c))
elif c >= 18.5 and c < 25 :
    print("\nSeu Imc é de {:.2f},\nE está com o peso ideal! ".format(c))
elif c >=25 and c < 30 :
    print("\nSeu Imc é de {:.2f},\nE está em sobrepeso!".format(c))
elif c >= 30 and c <= 40:
    print("\nSeu Imc é de {:.2f},\nE está em obesidade!".format(c))
else:
    print("\nSeu Imc é de {:.2f},\nE está em obesidade mórbida! ".format(c))

print("\n{:=^50}".format(" Fim "))
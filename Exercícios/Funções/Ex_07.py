

#def objetivo(a,b):
#    if a == 1:
#        resultado=b*2
#    elif a ==2:
#        resultado=b*3
#    elif a == 3:
#        resultado=b*4
#    return resultado

#a=int(input("\nEscolha a opção:\n\n1-Duplicar\n2-Triplicar\n3-Quadruplicar\n\nOpção: ").strip())
#b=int(input("\nDigite o numero que deseja: ").strip())

#print("\n",objetivo(a,b))

def um_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = um_multiplicador(2)
triplicar = um_multiplicador(3)
quadruplicar = um_multiplicador(4)

a=int(input("\nDigite o que deseja multiplicar: ").strip())
b=int(input("\nDigite o que deseja triplicar: ").strip())
c=int(input("\nDigite o que deseja quadruplicar: ").strip())

print('Duplicado: ',duplicar(a))
print("triplicado: ",triplicar(b))
print("Quadruplicado: ",quadruplicar(c))


#CODIGO DE JUGO DE PEDRA PAPEL E TESOURA.

from random import choice
from time import sleep
print("\n{:=^50}".format(" Pedra Papel e Tesoura "))

print("\nVamos jogar pedra papel e tesoura ?")

print("\n\n1 - Sim\n2 - Não")

a=int(input("\nDigite a Opção desejada: ").strip())

l=['pedra','papel','tesoura']
z=choice(l)

if a == 1:
    sleep(2)
    print("\nQue otimo!!\n\n Escolha as opções:\n\n1 - Pedra\n2 - Papel\n3 - Tesoura")

    b=int(input("\nEscolha uma das 3 opções: ").strip())
    
    if b == 1:
        print("PEDRA..")
        sleep(1)
        print("PAPEL..")
        sleep(1)
        print("TESOURAA!!")
        sleep(1)
        print("\nEu escolho {}".format(z))
        if z == l[0]:
            print("\nEmpatamos")
        elif z == l[1]:
            print("\nHahaa, eu ganhei!!")
        else:
            print("\nDroga.. Parabéns você ganhou!! ")

    elif b == 2:
        print("PEDRA..")
        sleep(1)
        print("PAPEL..")
        sleep(1)
        print("TESOURAA!!")
        sleep(1)
        print("\nEu escolho {}".format(z))
        if z == l[1]:
            print("\nEmpatamos")
        elif z == l[2]:
            print("\nHahaa, eu ganhei!!")
        else:
            print("\nDroga.. Parabéns você ganhou!! ")
    elif b == 3:
        print("PEDRA..")
        sleep(1)
        print("PAPEL..")
        sleep(1)
        print("TESOURAA!!")
        sleep(1)
        print("\nEu escolho {}".format(z))
        if z == l[2]:
            print("\nEmpatamos")
        elif z == l[0]:
            print("\nHahaa, eu ganhei!!")
        else:
            print("\nDroga.. Parabéns você ganhou!! ")
    else:
        print("\nHumm...")
        sleep(2)
        print("\nNenhuma das opções informadas foram digitas.\n\nO programa será encerrado...")
        sleep(2)

elif a == 2 :
    print("\nHumm...")
    sleep(2)
    print("\nQue pena!! tudo bem então, até uma proxima! :)")
    sleep(2)

else:
    print("\nHumm...")
    sleep(2)
    print("\nNão foi digitado nenhuma das opções informadas!\nO programa será encerrado!!")
    sleep(2)

print("\n{:=^50}".format(" Fim "))
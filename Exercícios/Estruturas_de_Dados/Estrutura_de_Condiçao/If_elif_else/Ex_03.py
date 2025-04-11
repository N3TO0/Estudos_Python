#CODIGO DE UM JOGO DE ADIVINHAÇÃO.

from random import randint
from time import sleep
n=randint(0,5)

print("\n\n{:=^50}".format(" Jogo da Sorte "))

b=int(input("\nTente adivinhar qual numero é de 0 a 5: ").strip())

print("Humm..")
sleep(2)

if b==n:
 print("\nParabéns você acertou!! o numero era {}".format(n))
else:
 print("\nQue pena, você errou! o numero era {} e não o {}!".format(n,b))

print("\n{:=^50}".format(" Fim "))
#JOGO DE ADIVINHAÇÃO
from random import choice
a=['BOLA','SACO','COMPUTADOR','RELOGIO']
print("\nQual palavra vc acha que ira ser sorteada?\n\n1 - bola\n2 - saco\n3 - computador\n4 - relogio\n")

print("\nLembrando que vc terá apenas 3 chances para acertar!")

for z in range (1,4):
    d=choice(a)
    while True:
        try:
            b=int(input("\nQual opção ira escolher?:").strip())
        except:
            print("\nDigitou errado! tente novamente\n")
            continue
        break
    c=(b-1)
    if d == a[c]:
            print('\nParabens,você acertou!!\nVocê escolheu "{}" e a palavra escolhida foi "{}"\n'.format(a[c],d ))
            break
    else:
        print('\nQue pena,você errou!\nVocê escolheu "{}" e a palavra escolhida foi "{}"\n'.format(a[c],d ))
        print(f"vc já usou {z} chance!")
        continue

print("\nFim\n")
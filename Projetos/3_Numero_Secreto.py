import random 

print("\n======== Jogo de Adivinhação ========")

print("\nAdivinhe o numero secreto de 1 a 10")

NUMERO_CORRETO = int(random.randint(0,10))

while True:
    
    try:
        Numero_Imput= int(input("\nDigite o numero: ").strip())

    except ValueError:
        print("\nValor digitado não é um numero, tente novamente!")
        continue

    if Numero_Imput < NUMERO_CORRETO:
        print("Numero secreto é maior")

    elif Numero_Imput > NUMERO_CORRETO:
        print("Numero secreto é menor")
        
    else:
        print(f"\nVocê acertou o numero secreto é '{NUMERO_CORRETO}'")
        break

print("\n========= fim do programa =========")


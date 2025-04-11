#JOGO PALAVRA SECRETA 

palavra_secreta = 'shoping'
letras_acertadas = ''
i = 1

while True:
    letra_digitada = input("\nDigite uma letra: ")

    if len(letra_digitada) > 1:
        print('\nDigite apenas uma letra!')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        print(f"\nParabéns, você acertou a palavra!\n {i} Tentativas")
        break

    i += 1
print("\n\nFim\n\n")

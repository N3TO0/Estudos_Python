print("\n======== Caixa Eletrônico ========")

saldo = 500

while True:
    print("\n Deseja: \n\n1 - Secar \n2 - Depositar \n3 - Verificar Saldo \n4 - Sair")

    Escolha_Inicial=int(input("\nOpação: ").strip()) # Input de escolha inical

    if Escolha_Inicial == 1:     # opção 1 -sacando
        try:
            sacando=int(input("Deseja sacar quanto ?")) # Input de valor saque
            

            if saldo < sacando : # Verificação de saldo insuficiente
                print("\nSaldo insuficiente")
            else:                # Verificação de saldo suficiente
                saldo -= sacando
                print(f"\n{sacando} foi sacado da conta!")
                print(f"\nConta tem saldo de R$ {saldo}")
                
        except ValueError:        # Verificaçãio de input com valor incorreto
            print("\nValor digitado não corresponde")

    elif Escolha_Inicial == 2: #opção 2 - depositando
        try:
            Depositando=int(input("\nDeseja sacar quanto ?"))
            saldo+= Depositando
            print(f"\n{Depositando} foi depositando na Conta! \nConta tem saldo de R$ {saldo}")

        except ValueError:       # Verificaçãio de input com valor incorreto
            print("\nValor digitado não corresponde")

    elif Escolha_Inicial == 3: #opção 3 - verificação de saldo
        print(f"\nConta tem saldo de R$ {saldo}")
    
    elif Escolha_Inicial == 4: #opção 4- sair do programa
        break

    else:
        print("\nOpção escolhida inexistente, tente novamente!") # Conseguencia de opção inical não correspondente

print("\n======== fim do programa ========")



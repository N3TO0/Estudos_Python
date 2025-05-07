#Caixa eletronico com funções (deposito, saquem extrato)

def Fun_deposito(saldo):
    try:
        Deposito=float(input("\nDigite o valor que deseja depositar: "))
        print("\n")
    except ValueError:
        erro2()
        return saldo
    
    if Deposito < 0: 
        erro2() 
        return saldo
    
    Extrato.append(f"Deposito: {Deposito:.2f}")
    return saldo + Deposito

def Fun_saque(saldo,acc):
    try:
        Saque=float(int(input("\nDigite o valor que deseja sacar: ")))
        print("\n")

    except ValueError:
        erro2()
        return saldo
    
    if Saque > saldo:
        erro2() 
        return saldo
    if Saque < 0:
        erro2() 
        return saldo

    if acc > 3 or Saque > 500:
        print("\nQuantidade de saques chegou ao limite | saque não pode ser maior que R$ 500!!\n")
        return saldo
    
    Extrato.append(f"Saque: {-Saque:.2f}")
    return saldo - Saque  
  
def Fun_extrato(Extrato): 
    print("EXTRATO".center(50,'-')) 

    if len(Extrato) == 0:
        print("\nNenhum valor depositado ou sacado!\n")
        print("".center(50,'-'))
        return 0
    for valores in Extrato: 
        print(f" R$ {valores}")

    print("".center(50,'-')) 

def Fun_saldo(saldo):
    return print(f"\nSaldo atual: R$ {saldo:.2f}\n")

def erro():
    return print("\nOpção digitada não corresponde, tente novamente!\n")

def erro2():
    return print("\nSaldo insuficiente | valor não corresponde\ntente novamente!\n")

Saldo = float(100)
Extrato = []
acc= 1

print("BANCO SHOW".center(50,'-'))

while True: #Lopping de opções
    try:
        Opcao=int(input("""
            Escolha a opção que deseja:
        
            1 - Deposito
            2 - Saque
            3 - Extrato
            4 - Saldo
            5 - Sair
            
            Opção: """ ))

    except  ValueError: #validação de tipo das opçãos fornecidas 
        erro()
        continue

    if Opcao not in (1, 2, 3, 4, 5): #validação das opções fornecidas
        erro()
        continue

    if Opcao == 1: #Funcionalidade da opção deposito
        Saldo=Fun_deposito(Saldo)
        Fun_saldo(Saldo)

    elif Opcao == 2 : #Funcionalidade da opção saque
        Saldo=Fun_saque(Saldo,acc)
        Fun_saldo(Saldo)
        acc+=1

    elif Opcao == 3: #Funcionalidade da opção Extrato
        Fun_extrato(Extrato)
        
    elif Opcao == 4: #Funcionalidade da opção Saldo
        Fun_saldo(Saldo)

    elif Opcao == 5: #Funcionalidade da opção sair
        print("\nTenha um otimo dia!\n")
        break
    
  
print("Fim".center(50,'-')) 
 
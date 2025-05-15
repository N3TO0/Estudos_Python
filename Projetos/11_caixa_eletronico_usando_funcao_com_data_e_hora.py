#Caixa eletronico com funções (deposito, saquem extrato)

from datetime import datetime, timezone, timedelta
import pytz

Saldo = float(100)
Extrato = []
hoje= datetime.now().strftime("Data: %d/%m/%Y | Hora: %H:%M")
solicitacoes_por_dia = {}


#Função para depositar
def Fun_deposito(saldo, Extrato, hoje):
    try:
        Deposito=float(input("\nDigite o valor que deseja depositar: "))
        print("\n")
    except ValueError:
        erro2()
        return saldo
    
    if Deposito < 0: 
        erro2() 
        return saldo
    
    Extrato.append(f"Deposito: R$ {Deposito:.2f} | {hoje}")
    return saldo + Deposito

#Função para sacar
def Fun_saque(saldo, Extrato, hoje):
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

    if hoje not in solicitacoes_por_dia:
        solicitacoes_por_dia[hoje]=0

    if solicitacoes_por_dia[hoje] < 10 and Saque < 500:
        solicitacoes_por_dia[hoje]+=1
        Extrato.append(f"Saque: R$ {-Saque:.2f} | {hoje}")
        return saldo - Saque  

        
    else:
        print("\nQuantidade de saques chegou ao limite ou Saque é maior que R$ 500!!\n")
        return saldo
    
    

#Função para verificar extrato
def Fun_extrato(Extrato): 
    print("EXTRATO".center(50,'-')) 

    if len(Extrato) == 0:
        print("\nNenhum valor depositado ou sacado!\n")
        print("".center(50,'-'))
        return 0
    for valores in Extrato: 
        print(f"\n {valores}\n")

    print("".center(50,'-')) 

#Função para verificar saldo
def Fun_saldo(saldo):
    return print(f"\nSaldo atual: R$ {saldo:.2f}\n")

#Função para sinalizar erro
def erro():
    return print("\nOpção digitada não corresponde, tente novamente!\n")

#Função para sinalizar erro
def erro2():
    return print("\nSaldo insuficiente | valor não corresponde\ntente novamente!\n")



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
        Saldo=Fun_deposito(Saldo, Extrato, hoje)
        Fun_saldo(Saldo)

    elif Opcao == 2 : #Funcionalidade da opção saque
        Saldo=Fun_saque(Saldo,Extrato, hoje)
        Fun_saldo(Saldo)

    elif Opcao == 3: #Funcionalidade da opção Extrato
        Fun_extrato(Extrato)
        
    elif Opcao == 4: #Funcionalidade da opção Saldo
        Fun_saldo(Saldo)

    elif Opcao == 5: #Funcionalidade da opção sair
        print("\nTenha um otimo dia!\n")
        break
    
  
print("Fim".center(50,'-')) 
 
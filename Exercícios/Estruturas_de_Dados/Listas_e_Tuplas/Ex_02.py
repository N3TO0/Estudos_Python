import os
lista = []


print("\nBem vindo a lista!")

while True:
    indices= range(len(lista))

    print(f"\nEssa é sua lista atualmente:")
    indice = 1
    for indice in indices:
        print(indice,"-",lista[indice])

    b=input("\n\nDeseja:\n\n1-Criar\n2-Editar\n3-Exluir\n4-Sair\n\nOpção: ").strip()
    print("-"*50)

    z=len(lista)
    
    if b == "1":
        os.system('cls')
        x=input("\nAcrescente um item a lista: ").strip()
        lista.append(x)

        continue
    if b == "2": 
        os.system('cls')       
        print(f"\nEssa é sua lista atualmente:\n")
        for indice in indices:
            print(indice,lista[indice])

        try:
            os.system('ccls')
            c=int(input(f"\nAtualmente a lista contem: {z} itens na lista\nDigite a posição do item para alterala:\n").strip()) # armazenará o indice
            t=input("\nDigite a alteração:") #armazenará a alteração 
            s=c-1 # correção da posição na lista
            lista.pop(s) #irá deletar o item do indice informardo 
            lista.insert(s, t) # irá inserir a alteração contendo na variavel t, no indice do item que foi deletado
        
        except:
            os.system('cls')
            print("\nValor digitado inexistente nas opções informadas, tente novamente!")
        continue

    if b == "3":
        os.system('cls')
        print(f"\nEssa é sua lista atualmente")
        for indice in indices:
            print(indice,lista[indice])

        try:
            os.system('cls')
            c=int(int(input(f"\nAtualmente a lista contem: {z} itens\nDigite a posição do item para Exluir: ").strip()))
            s=c-1
            del lista[s]

        except:
            os.system('cls')
            print("\nValor digitado inexistente nas opções informadas, tente novamente!")
        continue

    if b == "4":
        os.system('cls')
        print("\nFim")
        break

    else:
        os.system('cls')
        print("\nOpção escolhida não listada, por gentileza tente novamente!\n")
        print("-"*50)
        continue
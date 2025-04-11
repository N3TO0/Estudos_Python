#CODIGOQ UE VERIFICA SE FOI DIDITADO UM NUMERO INTEIRO E INFORMA SE É IMPAR OU PAR
try:
    a=int(input("\nDigite um numero inteiro: ").strip())

    if a % 2 == 0:
        print("\nÉ um numero Par")
    else:
        print("\nÉ um numero impar\n")
except:

    print("\nNão digitou um numero inteiro !\n")
    

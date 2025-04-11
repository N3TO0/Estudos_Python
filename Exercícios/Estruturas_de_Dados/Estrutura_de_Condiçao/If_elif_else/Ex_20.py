#CODIGO QUE ANALISA A QUANTIDADE DE CARACTERE E INFORMA SE É GRANDE OU NÃO 

a=(input("\nDigite seu nome:").strip())
b=len(a)

if b <= 4:
    print("\nSeu nome é curto!\n")

elif b >= 5 and b <= 6:
    print("\nSeu nome é normal!\n")

else:
    print("\nSeu nome é muito grande!\n")

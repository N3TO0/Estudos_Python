#CODIGO QUE VERIFICA OS DOIS PRIMEIROS CARACTERES E INFORMA A SAUDAÇÃO APROPRIADA.

a=str(input("\nDigite que horas são: "))
b=a[0:2]

if b >= "00" and b <= "11":
    print("\nBom dia!\n")

elif b >= "12" and b <= "17":
    print("\nBoa tarde!\n")

elif b >= "18" and b <= "23": 
    print("\nBoa noite!\n")

else:
    print("\nNão foi digitado corretamente!\n")
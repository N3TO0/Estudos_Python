#CODIGO QUE INFORMA SE A NOTA QUE TIROU FOI BOA OU RUIM.

a=int(input("\nDigite sua nota de 0 a 10: ").strip())
if a >= 9:
    print("Exelente")
elif a >= 7:
    print("Bom")
elif a >= 5:
    print("Rasoavel")
else:
    print("Insatisfatorio")
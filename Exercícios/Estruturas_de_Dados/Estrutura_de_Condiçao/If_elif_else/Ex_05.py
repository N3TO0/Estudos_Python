#CODIGO QUE INFORMA SE É IMPAR OU PAR.

print("\n{:=^50}".format(" Par ou Impar ? "))

b=int(input("\nDigite um numero para saber se é impar ou par: ").strip())
c=b%2

print("{} é um numero Par" if c==0 else " \n {} é um numero Impar".format(b,b))

#if c == 0:
#    print("{} É um numero par! ".format(b))
#else:
#    print("{} É um numero impar!".format(b))

print("\n{:=^50}".format(" Fim "))
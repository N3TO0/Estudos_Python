#TABUADA COM FOR.
print("\n{:=^50}".format(" Tabuada "))

print("Informe qual numero deseja saber a tabuada")

b=int(input("\nTabuada de: ").strip())

for c in range (0, 11):
    f=b*c
    print("{} x {} = {} ".format(b,c, f))
    
print("\n{:=^50}\n".format(" Fim "))


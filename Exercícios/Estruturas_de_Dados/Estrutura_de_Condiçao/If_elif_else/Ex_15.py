#CODIGO DE CONSULTA DE ALISTAMENTO

from datetime import date
print("\n{:=^50}".format(" Alistamento "))
a = date.today().year
b = int(input("\nAno de nascimento: ").strip())
c = a-b

if c == 18:
    print ("\nVocê tem {} anos, e precisa se alistar urgente!!".format(c))

elif c < 18:
    d= c-18 
    if c == 1:
        
        print("\nVocê tem {} ano, podera se alistar em {} anos !".format(c,d))
    else:
        print("\nVocê tem {} anos, e não pode se alistar ainda!\nMas podera em {} anos".format(c,b))
else:
    d= c-18
    if d >= 2:
        print("\nVocê tem {} anos, deveria ter se alistado a {} anos,\nentre entre em contato para saber como proceder e se alistar !!".format(c,d))
    else:
        print("\nVocê tem {} anos deveria ter se alistado a {} ano,\nentre entre em contato para saber como proceder e se alistar !!".format(c,d))
print("\n{:=^50}\n".format(" Fim "))
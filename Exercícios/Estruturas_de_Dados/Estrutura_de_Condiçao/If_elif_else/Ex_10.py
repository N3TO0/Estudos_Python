#CODIGO PARA SIMULAR ANALISE DE EMPRESTIMO.
from time import sleep

print("\n{:=^50}".format(" Emprestimo "))

a=float(input("\nqual o valor da casa ? : ").strip()) 
b=float(input("\nQual o valot total do seu salario ? : ").strip())  
c=float(input("\nDeseja quitar o Emprestimo em quantos anos ? : ").strip()) 
d=a/(c*12) 
e=(b*30)/100 

if d <= e:
    print("\ncalculando...")
    sleep(2)

    print("\nParabéns o emprestimo foi aprovado!!\nO valor da prestação é de: R$ {:.2f} ".format(d))

else:
    print("\ncalculando...")
    sleep(2)
    print("\nSinto muito mas o Emprestimo não foi aprovado!")


print("\n{:=^50}".format(" Fim "))

#CODIGO CONTAGEM REGRESSIVA PARA FOGOS
from time import sleep
print("\n{:=^70}".format(" Contagem Regreciva para Fogos de Artificio  "))

for c in range (10, -1 , -1):
    print("\nFalta {} Segundos para os fogos!!".format(c))
    sleep(1)

print("\n")
print("=" * 70 ) 
print("\nChegou a hora!!, olha que fogos lindos!!!")

print("\n{:=^70}\n".format(" Fim "))

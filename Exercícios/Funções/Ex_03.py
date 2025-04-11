

def multiplicacao (*args):
    total=1
    for numero in args:
        total *= numero
    return total


A=int(input('\nDigite a quantidade de numeros que deseja multiplicar: ').strip())

top=[]

for nu in range(A):
    b=int(input('\nDigite o valor:').strip())
    top.append(b)
s=multiplicacao(*top)
print('\nTotal da Multiplicação:',s)




def soma (x,y):
        return x+y

print('\nDigite dois valores para serem somados!')

while True:
    
    try:
          a=int(input('\nValor 1: ').strip())
          b=int(input('\nValor 2: ').strip())
    except ValueError:
          print('Valor digitado não é um numero,tente novamente!!')
          continue
    break

print(f"\n{a} + {b} = ",soma(a,b))
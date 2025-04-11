
def resultado(args):
    if args % 2 == 0:
        return '\nNumero Par!'
    else:
        return '\nNumero Impar!'
while (True):
    a=int(input('\nDigite o numero para saber se é ímpar ou par: ').strip())
    s=resultado(a)
    print(s)
    t=int(input("\nDeseja:\n\n1-Continuar\n2-Sair\n\nOpção: "))
    if t == 1:
        continue
    elif t == 2:
        break;
    else:
        print('\nOpção não reconhecida, tente novamente!')
        continue

print('Fim!')
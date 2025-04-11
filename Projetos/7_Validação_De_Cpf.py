#VALIDAÇÃO DE CPF

while True:

    cpf=input("Digite o cpf:")
    digitos_9 = cpf[:9] #armazenei apenas os 9 primeiros numeros
    multiplicador = 10 
    resultado=0
    p=cpf[0]* len(cpf)

    if cpf == p:
        print('cpf, invalido, tente novamente!')
        continue

    for contador in digitos_9:

        resultado = resultado + int(contador) * multiplicador
        multiplicador-= 1
        
    resultado = (resultado * 10) % 11

    if resultado >= 9:
        resultado=0

    digitos_10 = cpf[:10] #armazenei apenas os 10 primeiros numeros
    multiplicador = 11 
    resultado2=0

    for contador in digitos_10:

        resultado2 = resultado2 + int(contador) * multiplicador
        multiplicador-= 1
        
    resultado2 = (resultado2 * 10) % 11

    if resultado2 > 9:
        resultado2=0

    n_cpf = f'{digitos_9}{resultado}{resultado2}'
    if n_cpf == cpf:
        print("Cpf valido!")
        break
    else:
        print("Cpf invalido!")

#VALIDAÇÃO DE SENHA 
b=input("\nEscolha sua senha:").strip()

while True:
    try:
        v=input("\nDeseja entrar ? :\n\n1 - Sim\n2 - Não\n\nEscolha: ").strip().upper()
        if v == '1' or v == 'SIM':
            a=input("\nDigite a sua senha: ").strip()

        elif v == '2' or v == 'NÃO':
                break
        if a == b:
            print("\nVocê entrou no sistema!!")
            break
    except:
         print("Valor digitado errado, tente novamente!!")
         continue
    
print("\n\nFim")
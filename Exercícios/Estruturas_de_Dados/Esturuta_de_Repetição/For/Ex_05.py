#CODIGO PARA SIMULAR SENHA

print("\nDigite a sua senha corretamente\n")

s2 ='123456'

for c in range(6):

    s1 = input("Senha: ").strip()

    if s1 == s2:
        print('Bem vindo')
        break  
else:
    print('Limite de senha alcançado!') 
        
print('Fim') 
      


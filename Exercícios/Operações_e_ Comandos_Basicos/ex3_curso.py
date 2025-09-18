#1. Elaborar um programa que apresente o resultado da soma e da média aritmética dos valores pares situados entre 40 e 70 (inclusive)

contador_numeros_pares=0
soma_numeros_pares=0

for repetidor in range(40,71,1):

    if repetidor % 2 == 0:
        contador_numeros_pares+=1
        soma_numeros_pares+=repetidor

print(f"\nExistem {contador_numeros_pares} numeros pares entre 40 e 70")
print(f"\nA soma de todos os numeros pares de 40 a 70 é: {soma_numeros_pares}")
print(f"\nA media aritmética dos numeros pares de 40 a 70 é: {soma_numeros_pares / contador_numeros_pares}\n\n")

# ---------------------------------------------------------------------------------------

#2. Leia a idade de 20 pessoas e exiba quantas pessoas são maiores de idade.

# mariores_de_idade=0

# for contador in range(20):
    
#     idade=int(input("\nDigite sua idade: "))
#     if idade >= 18:
#         mariores_de_idade+=1

# print(f"\n{mariores_de_idade} pessoas são maiores de idade!\n")

# ---------------------------------------------------------------------------------------

# 3. Leia o nome e a idade de 10 pessoas e exiba o nome da pessoa mais nova.

# menor_idade=0

# for contador in range(10):
    
#     idade=int(input("\nDigite sua idade: "))
#     if contador == 0: menor_idade=idade
        
#     elif menor_idade > idade: menor_idade=idade
        
# print(f"\nA pessoa mais nova tem {menor_idade} anos\n")

# ---------------------------------------------------------------------------------------

# 4. Crie uma variável que vai armazenar a palavra secreta “Programação”. 
# Em seguida, utilize uma estrutura de repetição que deve parar de solicitar uma palavra apenas quando o usuário acertar a palavra secreta.

# PALAVRA_SECRETA="shopping"

# tentativas=0
# palavras_acertadas_salvas=""

# print("\nTente acertar a palavra secreta!\n")
# while True:

#     palavra_sensurada_com_letra_acertada =""

#     letra_digitada=input("\nDigite uma letra: ")
    
#     if letra_digitada in PALAVRA_SECRETA:
#         print("\nVocê acertou uma letra!")
#     else:
#         print("\nVocê errou a letra!")

#     for letra in PALAVRA_SECRETA:
#         if letra == letra_digitada or letra in palavras_acertadas_salvas:
            
#             palavras_acertadas_salvas+=letra_digitada
#             palavra_sensurada_com_letra_acertada+=letra
#         else:
            
#             palavra_sensurada_com_letra_acertada+="*"
    
#     print("\n",palavra_sensurada_com_letra_acertada,)            
    
#     if palavra_sensurada_com_letra_acertada == PALAVRA_SECRETA:
#         break

# print(f"\nVocê acertouuu em {tentativas}, parabenss !!🎉\n\n")

# -----------------------------------------------------------------------------

# 5. Escrever um programa que leia um conjunto de 50 informações contendo, cada uma delas,
# a altura e o sexo biológico de uma pessoa (1 - masculino 2-feminino), calcule e mostre o seguinte: 

# a) a maior e a menor altura da turma
# b) a média da altura das mulheres
# c) a média da altura da turma.

# altura_sexo_feminino=[]
# altura_da_turma=[]

# menor_altura_turma=0
# maior_altura_turma=0

# for contador in range(3):
#     altura=float(input("\n\nDigita a sua altura: "))
#     sexo=int(input("Digite seu sexo biológico:\n\n1 - Masculindo\n2 - Feminino \n\nMeu sexo é: "))
    
#     if contador == 0:
#         menor_altura_turma=altura
#         maior_altura_turma=altura

#     else:
#         if altura < menor_altura_turma : menor_altura_turma = altura
#         if altura > maior_altura_turma : maior_altura_turma = altura

#     if sexo == 2:
#         altura_sexo_feminino.append(altura)
#     altura_da_turma.append(altura)
        
# media_turma=sum(altura_sexo_feminino) / len(altura_sexo_feminino)
# media_feminino=sum(altura_da_turma) / len(altura_da_turma)

# print(f"\n\nMaior altura da turma: {maior_altura_turma:.2f}")
# print(f"Menor altura da turma: {menor_altura_turma:.2f}")
# print(f"Media da altura da turma: {media_turma:.2f}")
# print(f"Media da altura do sexo feminino: {media_feminino:.2f}\n\n")

# -----------------------------------------------------------------------------

# 6. Desenvolva um programa em Python para registrar informações sobre funcionários em uma empresa. Comece solicitando o número de funcionários. 
# Para cada funcionário, o programa deve requisitar o nome, salário e departamento (“Vendas”, “RH” ou “Gerência”). Ao final, apresente as seguintes estatísticas:

# ● O nome do funcionário com o salário mais alto.
# ● A média dos salários dos funcionários.
# ● A quantidade de funcionários que trabalham no departamento de Vendas.

departamento_vendas=[]
media_dos_salarios=0
nome_do_funcionario_com_maior_salario=""
maior_salario=0

numero_de_funcionarios=int(input("\nDigite a quantidade de funcionarios: ").strip())

for contador in range(numero_de_funcionarios):

    nome_funcionario=input("\nDigite seu nome: ").strip()
    salario=int(input("\nInforme seu salario: ").strip())
    departamento=int(input("\nInforme seu departamento:\n\n1 - Vendar\n2 - Rh\n3 - Gerência\n\nDigite seu departamento: ").lower().strip())

    if departamento == 3 : departamento_vendas.append(contador)

    if contador == 0 : 
        maior_salario = salario 
        nome_do_funcionario_com_maior_salario = nome_funcionario

    else: 
        if salario > maior_salario:
            maior_salario = salario 
            nome_do_funcionario_com_maior_salario = nome_funcionario

    media_dos_salarios += salario
    
print(f"\n\nO nome do funcionario com o salário mais alto é: {nome_do_funcionario_com_maior_salario}")
print(f"A média dos solários dos funcionarios é: R$ {(media_dos_salarios/numero_de_funcionarios):.2f}")
print(f"A quantidade de funcionários que trabalham no departamento de vendas é: {len(departamento_vendas)}\n\n")
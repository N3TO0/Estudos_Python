# 1 - Carregue uma lista com 20 números inteiros e
# armazene em outra lista apenas os números pares e outra os ímpares.

print("\nDigite 20 muneros:\n\n")
lista_numeros_inteiros=[int(input(f"{contador+1}° Numero: ")) for contador in range(5)]

lista_pares=[numero for numero in lista_numeros_inteiros if numero % 2 == 0 and numero > 0]
lista_impares=[numero for numero in lista_numeros_inteiros if numero % 2 != 0]

print(f"pares: {lista_pares} ")
print(F"inpares: {lista_impares}")



# ---------------------------------------------------------------------------
# 2 - Faça um programa que leia duas listas com 10 elementos cada. Gere
# uma terceira lista, cujos valores deverão ser compostos pelos elementos
# intercalados dos dois outros vetores.


lista1=[1,2,3,4,5,6,7,8,9,10]
lista2=[11,12,13,14,15,16,17,18,19,20]
lista3=[]

for contador in range(10):
    
    lista3.append(lista1[contador])
    lista3.append(lista2[contador])

print(lista3)



# ---------------------------------------------------------------------------

# 3 - Fazer um programa para ler uma lista de 5 elementos, e, em
# seguida, mostrar a posição(não o índice) onde se encontram o maior e o
# menor valor e seus respectivos valores.

print()

lista=[ int(input(f"Informe o {posicao+1}° numero: ")) for posicao in range(5)]


print(f"\n\nO maior elemento é {max(lista)} e tem a posição {lista.index(max(lista))+1}\n")
print(f"O menor elemento é {min(lista)} e tem a posição {lista.index(min(lista))+1}\n")





# ---------------------------------------------------------------------------

# 4 - Ler uma sequência de números reais e armazená-los. A sequência
# termina quando for digitado o número (0) zero. Determinar o maior
# elemento dessa sequência e imprimir a lista resultante.

numero_real=[]

while True:
    numero_real.append(int(input("\nDigite um numero: ")))
    if numero_real[-1] == 0: break

print(f"\nO maior elemento é: {max(numero_real)}\n")
print("A lista é composta por: ")

for elemento in numero_real:
    print(f"Numero real: {elemento}")
print()

# ---------------------------------------------------------------------------

# 5 - Durante o planejamento de uma obra, um engenheiro registrou a
# quantidade de sacos de cimento utilizados em cada um dos 7 dias da
# semana. Escreva um programa em Python que leia a quantidade de sacos
# para cada dia e exiba o total de sacos de cimento usados na semana. Crie
# uma nova lista apenas com os dias em que o consumo foi acima de 29 sacos
# (utilize list comprehension) e exiba essa lista.

quantidade_de_cimentos_em_dias=[int(input(f"\nDigite a quantidade de cimento no {contador+1}° dia: ")) for contador in range(7) ]

total_cimento_na_semana=sum(quantidade_de_cimentos_em_dias)

dias_com_mais_de_29_sacos_usados=[ f"{indice+1}° dia" for indice ,valor in enumerate(quantidade_de_cimentos_em_dias) if valor > 29]

print("\nOs dias que foram utilizados mais e 29 sacos de cimento foram: \n")

if  len(dias_com_mais_de_29_sacos_usados) == 0:
    print("Nenhum dia teve mais de 29 sacos usados")

else:
    for elemento in dias_com_mais_de_29_sacos_usados:
        print(elemento)



# ---------------------------------------------------------------------------

# 6 - Faça um programa para corrigir provas de múltipla escolha. Cada
# prova contém 10 questões. A primeira lista a ser carregada é o gabarito
# da prova. Os outros dados são os números de matrícula dos alunos e as
# respostas que   deram às questões.
# Considere que temos 10 alunos. Calcule e mostre o número da matrícula e
# a nota de cada aluno. Mostre também a porcentagem de aprovação.


matriculas=[]
notas=[]
contador_aprovação=0
total_de_alunos=10

print()
gabarito_lista=[ input(f"Gabarto {contador+1}° questão: ").lower() for contador in range(10) ]

for contador in range(10):
    print()
    matriculas.append(input(f"Digite a matricula do {contador+1}° aluno: "))
    print()
    notas.append([(input(f"Digite a  resposta da {questao+1}° Questão:  ")).lower() for questao in range(10)])

for contador_primario in range(len(matriculas)):

    print(f"\n matricula: {matriculas[contador_primario]}:\n")

    contador_acertos=0

    for contador_segundario in range(len(gabarito_lista)):

        if notas[contador_primario][contador_segundario] == gabarito_lista[contador_segundario]:
            contador_acertos+=1
            print(f"{contador_segundario+1}° questão está Correta!")
        else:
            print(f"{contador_segundario+1}° quesão está Errada!")
    
    if contador_acertos >= 6 :
        contador_aprovação+=1
        print(f"\n\nAluno com Matricula {matriculas[contador_primario]} está Aprovado com nota {contador_acertos} !!")
    elif contador_acertos < 6 :
        print(f"\n\nAluno com Matricula {matriculas[contador_primario]} está Reprovado com nota {contador_acertos} !!")

    input("\nAperte 'ENTER' para seguir: ")

porcentual_aprovacao = float(( contador_aprovação / total_de_alunos ) * 100)

print(f"\nO porcentual de aprovação é de : {porcentual_aprovacao:.2f}%\n")
    
    

            




# ---------------------------------------------------------------------------

# 7 - Faça um programa que

# receba o nome de cinco produtos e seus respectivos preços, armazene-os
# em listas, calcule e mostre: 

# a) a quantidade de produtos com preço inferior a R$ 50,00; 
# b) o nome dos produtos com preço entre R$ 50,00 e R$ 100,00; 
# c) a média dos preços dos produtos com preço superior a R$ 100;

dados=["Nome","Valor"]
lista_nome_valor=[]
lista_entre_50_e_100=[]
lista_maior_100=[]
menor_que_50 = 0

for contador in range(5):
    lista_nome_valor.append([input(f"\nDigite o {elemento} do produto: ") for elemento in dados ])

for lista in lista_nome_valor:
    if int(lista[1]) < 50:
        menor_que_50+=1

    elif int(lista[1]) >=50 and int(lista[1]) <= 100:
        lista_entre_50_e_100.append(lista)

    else:
        lista_maior_100.append(float(lista[1]))

print(f"\nA quantidade de produtos com preço inferiros a R$50,00:\n\n{menor_que_50} produtos")

print("\nNomes e preços dos produtos com valores entre R$50,00 e R$100,00:\n")

for lista in lista_entre_50_e_100:
    for indice, elemento in enumerate(lista):
        print(f"{dados[indice]}: {elemento}")

print("\nA media dos produtos com preço superior a R$100,00: \n")

if not lista_maior_100:
    media=0
else:
    media= (sum(lista_maior_100) / len(lista_maior_100))

print(f"Media: R$ {media:.2f}\n")
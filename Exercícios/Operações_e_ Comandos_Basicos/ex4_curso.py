# 1 - Carregue uma lista com 20 números inteiros e
# armazene em outra lista apenas os números pares e outra os ímpares.

# print("\nDigite 20 muneros:\n\n")
# lista_numeros_inteiros=[int(input(f"{contador+1}° Numero: ")) for contador in range(5)]

# lista_pares=[numero for numero in lista_numeros_inteiros if numero % 2 == 0 and numero > 0]
# lista_impares=[numero for numero in lista_numeros_inteiros if numero % 2 != 0]

# print(f"pares: {lista_pares} ")
# print(F"inpares: {lista_impares}")



# ---------------------------------------------------------------------------
# 2 - Faça um programa que leia duas listas com 10 elementos cada. Gere
# uma terceira lista, cujos valores deverão ser compostos pelos elementos
# intercalados dos dois outros vetores.


# lista1=[1,2,3,4,5,6,7,8,9,10]
# lista2=[11,12,13,14,15,16,17,18,19,20]
# print(lista1)
# print(lista2)





# ---------------------------------------------------------------------------

# 3 - Fazer um programa para ler uma lista de 5 elementos, e, em
# seguida, mostrar a posição(não o índice) onde se encontram o maior e o
# menor valor e seus respectivos valores.

# lista=[ int(input(f"Informe o {contador+1}° numero: ")) for contador in range(5)]
# maior_numero=0
# menor_menor=0

# for elemento in lista:
    
#     if elemento == lista[0]:
#         maior=elemento
#         menor=elemento

#     if elemento > maior: maior = elemento
#     if elemento < menor: menor = elemento

# for contador in range(len(lista)):

#     if maior == lista[contador]: print(f"\n\nO maior elemento é {maior} e tem a posição {contador+1}\n")
#     if menor == lista[contador]: print(f"O menor elemento é {menor} e tem a posição {contador+1}\n")







# ---------------------------------------------------------------------------

# 4 - Ler uma sequência de números reais e armazená-los. A sequência
# termina quando for digitado o número (0) zero. Determinar o maior
# elemento dessa sequência e imprimir a lista resultante.

# ---------------------------------------------------------------------------

# 5 - Durante o planejamento de uma obra, um engenheiro registrou a
# quantidade de sacos de cimento utilizados em cada um dos 7 dias da
# semana. Escreva um programa em Python que leia a quantidade de sacos
# para cada dia e exiba o total de sacos de cimento usados na semana. Crie
# uma nova lista apenas com os dias em que o consumo foi acima de 29 sacos
# (utilize list comprehension) e exiba essa lista.


# ---------------------------------------------------------------------------

# 6 - Faça um programa para corrigir provas de múltipla escolha. Cada
# prova contém 10 questões. A primeira lista a ser carregada é o gabarito
# da prova. Os outros dados são os números de matrícula dos alunos e as
# respostas que   deram às questões.
# Considere que temos 10 alunos. Calcule e mostre o número da matrícula e
# a nota de cada aluno. Mostre também a porcentagem de aprovação.


# gabarito_lista=[]
# matriculas_e_respostas=[]


# for questao in range(10):

#     gabarito_resposta=input(f"\nGabarito da questão {questao}°: ")
#     gabarito_lista.append(gabarito_resposta)

# numero_de_alunos=int(input("Informe a quantidade de alunos: "))

# for alunos in range(numero_de_alunos):
    
#  for notas in range(10):

        
    
    

            




# ---------------------------------------------------------------------------

# 7 - Faça um programa que

# receba o nome de cinco produtos e seus respectivos preços, armazene-os
# em listas, calcule e mostre: a) a quantidade de
# produtos com preço inferior a R$ 50,00; b) o nome dos produtos
# com preço entre R$ 50,00 e R$ 100,00; c) a
# média dos preços dos produtos com preço superior a R$ 100;
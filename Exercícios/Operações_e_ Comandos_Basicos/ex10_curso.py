#1) Leitura de uma lista de inteiros com tratamento de exceções: Criar um programa 
# que leia uma lista de até 10 inteiros. A entrada de valores deve ser interrompida
# ao digitar zero, que também deve ser inserido na lista. O programa deve tratar
# as seguintes exceções:

# RuntimeError se mais de 10 valores forem informados ("Tamanho do vetor 
# previsto foi excedido.").

# ValueError se um valor não inteiro for informado ("Tipo inválido.").

# codigo:

# def leiturra_de_lista(lista):
#     print(lista)
     
#     lista=[]
#     numero_maximo = 10

#     while True:
#         try:
#             if len(lista)>= numero_maximo:
#                 raise RuntimeError("\nTamanho de lista exedeu ao limite de 10 itens!")
        
#             entrada=int(input("\nDigite um numero intiero ( Ou zero caso deseje finalizar ): ").strip())

#             valor = int(entrada)

#             if valor == 0:
#                 lista.append(entrada)
#                 print("\nfinalizando Leitura!")
#                 break

#             lista.append(entrada)

#         except ValueError:
#             print("\nTipo inválido (Valor não inteiro informado!)")
        
#         except RuntimeError as erro_run:
#             print(f"\n{erro_run}")

#     return lista

# lista_final=leiturra_de_lista()

# print(f"\nLista Final tem {len(lista_final)} itens: {lista_final}")


# ------------------------------------------------------------------------------

# 2) Cálculo de FGTS com validação de entrada: Desenvolver um programa que solicite 
# o nome e o salário do usuário para calcular o valor do FGTS (8% do salário). As 
# validações são:

# Nome: entre 5 e 50 caracteres e não pode conter números.

# Salário: deve ser um número e igual ou superior a R$ 1100,00.

# Ao final, o programa deve imprimir o nome, salário e o valor do FGTS.

# codigo:

# import re
# filtro= r'\d'


# while True:

#     try:
#         nome=input("\nDigite seu nome: ").strip()

#         if len(nome) < 5 or len(nome) > 50:
#             print(f"\nNome precisa ter mais de 5 caracteres e menos de 50 caracteres!")
#             continue
        
#         filtragem= re.findall(filtro, nome)

#         if filtragem:
#               print("Nome não pode ter numero!")
#               continue
        
#         salario=float(input("Digite o valor do seu salário:"))

#         if salario < 1100:
#             print("\nNecessita ser maior que 1100!")
#             continue

#         fgts= (salario * 8) / 100

#     except ValueError as v:
#         print(f"\nValor inserido não é um numero!\n{v}")
#         continue


#     break

# print(f"\nNome: {nome}\nSalário: {salario:.2f}\nValor do FGTS (8%): R$ {fgts:.2f}\n")

# ------------------------------------------------------------------------------

# 3) Verificação de número perfeito: Criar um script que solicite um número inteiro e 
# verifique se ele é perfeito (soma dos divisores positivos menores que ele é igual 
# ao próprio número). O número deve ser maior que zero e menor ou igual a 32767. As 
# mensagens de erro incluem "Erro: dado inválido" e "Erro: o número deve ser maior que zero.".

# codigo:

# while True:
#     try:

#         numero = int(input("\nDigite um número inteiro (1 a 32767): ").strip())

#         if numero <= 0 and numero > 32767:
#             print("Erro: o número deve ser maior que zero. e manor ou igual a 32767")
#             continue 


#     except ValueError:
#         print("Erro: dado inválido, valor não é um numero!.")
#         continue
#     break

# soma_divisores = 0

# for divisor in range(1, numero):
#     if numero % divisor == 0:
#         soma_divisores += divisor

# if soma_divisores == numero:
#     print(f"\nO número {numero} É um número perfeito.")
# else:
#     print(f"\nO número {numero} NÃO é um número perfeito.")

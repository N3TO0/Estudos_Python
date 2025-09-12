# Round 1: O Aquecimento

# Dada a lista de números abaixo, crie uma nova lista chamada dobro onde 
# cada número da lista original seja multiplicado por 2.

numeros = [1,2,3,4,5,6,7,8,9,10]

dobro=[(numero*2) for numero in numeros]

[print(numero_dobro) for numero_dobro in dobro]

# Round 2: O Filtro Preciso

# Dada a lista de palavras abaixo, crie uma nova lista chamada 
# palavras_longas que contenha apenas as palavras com 5 ou mais caracteres.

palavras = ["python", "é", "uma", "linguagem", "poderosa", "e", "versátil"]

palavras_longas=[ palavra for palavra in palavras if len(palavra) >= 5]

[print(palavra) for palavra in palavras_longas]

# Round 3: A Combinação de Golpes

# Usando a mesma lista numeros do Round 1, crie uma nova lista chamada 
# quadrado_dos_pares que contenha o quadrado (número elevado a 2) apenas dos números pares da lista original.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrado_dos_pares = [(numero**2) for numero in numeros if numero % 2 == 0]

[print(numero) for numero in quadrado_dos_pares]



# Round 4: Trabalhando com Strings

# Dada a lista de nomes abaixo, crie uma nova lista chamada nomes_com_a que contenha todos os 
# nomes convertidos para minúsculas, mas somente se o nome original começar com a letra "A".

nomes = ["Amanda", "Ricardo", "Ana", "Felipe", "Antônio", "Beatriz"]

nomes_com_a =[ palavra.lower() for palavra in nomes if palavra[0] == "a" or palavra[0] == "A"]

[print(nome) for nome in nomes_com_a]



# Desafio Final: O Golpe Mestre (com if/else)

# Essa é para testar a flexibilidade! Dada a lista de números, crie uma nova lista chamada par_ou_impar. 
# Para cada número na lista original, a nova lista deve conter a 
# string "par" se o número for par, e a string "ímpar" se o número for ímpar.

# Dica: A sintaxe para if/else dentro de uma list comprehension é um pouco 
# diferente: [valor_se_verdadeiro if condicao else valor_se_falso for item in lista].

numeros = [1, 2, 3, 4, 5, 6]

par_ou_impar=[ "par" if numero % 2 == 0 else "impar" for numero in numeros]

[print(elemento) for elemento in par_ou_impar]
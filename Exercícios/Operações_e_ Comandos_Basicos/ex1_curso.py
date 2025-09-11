nota1= int(input("\nInforme a primeira nota da matéria: "))
nota2= int(input("\nInforme a segunda nota da matéria: ")) 

print(f"\nA média entre a nota: {nota1} e a nota: {nota2} é igual a {(nota1 + nota2)/2}\n")

# ---------------------------------------------------------------------------

dinehiro_na_carteira = float(input("\nInforma quanto dinheiro você tem: "))

print(f"\nVocê pode comprar:\nUS$ {(dinehiro_na_carteira / 5.50):.2f} \n")

# ---------------------------------------------------------------------------

altura=float(input("\nInforme a altura da parede em cm: "))
largura=float(input("\nInforma a largura da parede em cm: "))

area= (altura/100) + (largura/100)

baldes_de_tinta = area / 2

if baldes_de_tinta <= 2:
    print(f"\nA área a ser pintada é de {area:.1f} Metros Quadrados")
    print(f"São necessarios {baldes_de_tinta:.0f} Lata de tinta para pintar toda a parede!\n")
else:
    print(f"\nA área a ser pintada é de {area:.1f} Metros Quadrados\n")
    print(f"São necessarios {baldes_de_tinta:.0f} Latas de tinta para pintar toda a parede!\n")

# # --------------------------------------------------------------------------

total_eleitores=int(input("\nInforme o total de eleitores do municipio: "))
votos_brancos=int(input("\nInforme a quantidade de votos em branco: "))
votos_nulos=int(input("\nInforme a quantidade de votos nulos: "))
votos_validos=int(input("\nInforme a quantidade de votos validos: "))

total_de_votos= votos_validos + votos_brancos + votos_nulos

if total_de_votos < total_eleitores :
    print("\nOs dados não condizem com a quantidade eleitores! \n")
else:
    print(f"\nVotos Nulos: {((votos_nulos*total_eleitores)/100):.2f}%")
    print(f"Votos Válidos: {((votos_validos*total_eleitores)/100):.2f}%")
    print(f"Votos Brancos: {((votos_brancos*total_eleitores)/100):.2f}%\n")

# # --------------------------------------------------------------------------

salarios_atual=float(input("\nInforme o valor do seu salário atual: "))
porcentagem=float(input("\nInforme a porcentagem do aumento: "))

novo_salario= ((porcentagem * salarios_atual) / 100) + salarios_atual

print(f"\nO seu novo salário é R$ {novo_salario:.2f}\n")

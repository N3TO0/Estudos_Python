NOTA1= int(input("\nInforme a primeira nota da matéria: "))
NOTA2= int(input("\nInforme a segunda nota da matéria: ")) 

print(f"\nA média entre a {NOTA1} e {NOTA2} é igual a {(NOTA1 + NOTA2)/2}\n")

# ---------------------------------------------------------------------------

DINHEIRO_NA_CARTEIRA = float(input("\nInforma quanto dinheiro você tem: "))

print(f"\nVocê pode comprar:\n10US$ {(DINHEIRO_NA_CARTEIRA / 5.50):.2f} \n")

# ---------------------------------------------------------------------------

ALTURA=float(input("\nInforme a altura da parede em cm: "))
LARGURA=float(input("\nInforma a largura da parede em cm: "))

AREA= (ALTURA/100) + (LARGURA/100)

BALTES_DE_TINTA = AREA / 2

if BALTES_DE_TINTA <= 2:
    print(f"\nA área a ser pintada é de {AREA:.1f} Metros Quadrados\nSão necessarios {BALTES_DE_TINTA:.0f} Lata de tinta para pintar toda a parede!\n")
else:
    print(f"\nA área a ser pintada é de {AREA:.1f} Metros Quadrados\nSão necessarios {BALTES_DE_TINTA:.0f} Latas de tinta para pintar toda a parede!\n")

# --------------------------------------------------------------------------

TOTAL_ELEITORES=int(input("\nInforme o total de eleitores do municipio: "))
VOTOS_BANCO=int(input("\nInforme a quantidade de votos em branco: "))
VOTOS_NULOS=int(input("\nInforme a quantidade de votos nulos: "))
VOTOS_VALIDOS=int(input("\nInforme a quantidade de votos validos: "))

TOTAL_DE_VOTOS= VOTOS_VALIDOS + VOTOS_BANCO + VOTOS_NULOS

if TOTAL_DE_VOTOS < TOTAL_ELEITORES :
    print("\nOs dados não condizem com a quantidade eleitores! \n")
else:
    print(f"\nVotos Nulos: {((VOTOS_NULOS*TOTAL_ELEITORES)/100):.2f}%")
    print(f"Votos Válidos: {((VOTOS_VALIDOS*TOTAL_ELEITORES)/100):.2f}%")
    print(f"Votos Brancos: {((VOTOS_BANCO*TOTAL_ELEITORES)/100):.2f}%\n")

#--------------------------------------------------------------------------

SALARIO_ATUAL=float(input("\nInforme o valor do seu salário atual: "))
PORCENTAGEM=float(input("\nInforme a porcentagem do aumento: "))

NOVO_SALARIO= ((PORCENTAGEM * SALARIO_ATUAL) / 100) + SALARIO_ATUAL

print(f"\nO seu novo salário é R$ {NOVO_SALARIO:.2f}\n")
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Constantes
PONTUACOES = [".", ",", "?", "!", ":", ";"]

# Entrada do usuário
print(
    "Como você prefere digitar as frases?\n\n"
    "1 - Tudo de uma vez só (separadas por ponto)\n"
    "2 - Uma por vez (digite 'fim' para encerrar)\n"
)

while True:
    try:
        modo_entrada = int(input("Digite 1 ou 2 para escolher o modo de entrada: "))
        if modo_entrada == 1:
            texto = input("Digite a(s) frase(s): ").strip().lower()
            break
        elif modo_entrada == 2:
            lista_frases = []
            while True:
                frase_usuario = input("Digite uma frase: ").strip().lower()
                if frase_usuario == "fim":
                    break
                lista_frases.append(frase_usuario)
            texto = " ".join(lista_frases)
            break
        else:
            print("Opção inválida. Digite 1 ou 2.")
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros (1 ou 2).")

# Entrada do número de palavras mais frequentes
while True:
    try:
        limite_top_palavras = int(input("Escolha o número de top X palavras mais usadas: ").strip())
        break
    except ValueError:
        print("Valor digitado não corresponde, por favor digite novamente!")
        continue
# Remover pontuações
for simbolo in PONTUACOES:
    texto = texto.replace(simbolo, "")

# Separar palavras
lista_palavras = texto.split()

# Criar dicionário de frequência
dicionario_frequencias = {}
for palavra in lista_palavras:
    if palavra in dicionario_frequencias:
        dicionario_frequencias[palavra] += 1
    else:
        dicionario_frequencias[palavra] = 1

# Ordenar e mostrar palavras mais frequentes
palavras_mais_frequentes = sorted(
    dicionario_frequencias.items(), key=lambda item: item[1], reverse=True
)[:limite_top_palavras]

for posicao, (palavra, frequencia) in enumerate(palavras_mais_frequentes, start=1):
    print(f"Top {posicao}:\nPalavra: {palavra}\nRepetições: {frequencia}\n")

# Gerar a wordcloud
nuvem = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(dicionario_frequencias)

plt.figure(figsize=(10, 5))
plt.imshow(nuvem, interpolation='bilinear')
plt.axis("off")
plt.title("Nuvem de Palavras")
plt.show()

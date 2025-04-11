def repeticao(a,x):
    return a * x

while True:
    try:
        a=str(input("\nDitie uma letra: ").strip())
        x=int(input("\nDigite um numero: ").strip())

    except ValueError:
        print("\nValor não corresponde a solicitação, tente novamente!!")
        continue
    print(f"\n{repeticao(a,x)}\n")
    break


def even_or_odd(numero):
    if numero % 2 == 0:
        return f"\n{numero} é par\n"
    return f"\n{numero} é impar\n"
    

numero=int(input("\nDigite um numero: ").strip())

print(even_or_odd(numero))
#Calculadora
while True:
    
    try: 
        b=int(input("\n[1]Somar\n[2]Subrtair\n[3]Dividir\n[4]Multiplicar\n[5]Sair\n\nEscolha a opção: ").strip().upper())
        if b == 5:
            break

        c=float(input("\nValor 1: ").strip()) #Valor 1
        d=float(input("Valor 2: ").strip()) #Valor 2

    except:
        print("\nValor digitado é invalido, tente novamente") #Caso ocorra erro em digitar o valor correto
        continue
 
    if b == 1: #Somar
        print(c+d)
    elif b == 2: #Subtrair
        print(c-d)
    elif b == 3: #Dividir
        print(c/d)
    elif b == 4: #Multiplicar
        print(c*d)
    else: #Não digitou a numeração correta
        print("\nNão Digitou Corretamente")
        continue
    a=input("\nDeseja sair ? [S]im: ").upper().strip() #Sair da calculadora
    if a == 'S':
        break
    
    continue # lop caso escreva qualquer coisa menos S
    
print("\nFim\n")
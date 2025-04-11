x='shopping' #palavra secreta
v=''         #letras acertadas armazenadas
k=0
while True:
    
    i=input("\nAdivinha uma letra da palavra secreta: ")
   
    if len(i) > 1:
        print("\nDigite apenas uma letra!, por favor tente novamente!")
        continue

    if i in x :
        v += i   #letras acertadas
    t ="" # letras comparadas contendo no iterador x, no loop do for
    for a in x:
        if a in v :
            t+=a # t recebe o valor se a estiver dentro de v
        else:
            t+='*' # t recebe o valor * se a não tiver o valor dentro de v
    k+=1 #contador de vezes jogadas
    print(t) 
    if t == x:
        print(f"\nParabens você venceu, e levou {k} rodadas para conseguir!")
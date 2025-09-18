matriculas=[]
notas=[]
contador_aprovação=0

print()
gabarito_lista=[ input(f"Gabarto {contador+1}° questão: ").lower() for contador in range(10) ]

for contador in range(10):
    print()
    matriculas.append(input(f"Digite a matricula do {contador+1}° aluno: "))
    print()
    notas.append([(input(f"Digite a  resposta da {questao+1}° Questão:  ")).lower() for questao in range(10)])

for contador_primario in range(len(matriculas)):

    print(f"\n matricula: {matriculas[contador_primario]}:\n")

    contador_acertos=0

    for contador_segundario in range(len(gabarito_lista)):

        if notas[contador_primario][contador_segundario] == gabarito_lista[contador_segundario]:
            contador_acertos+=1
            print(f"{contador_segundario+1}° questão está Correta!")
        else:
            print(f"{contador_segundario+1}° quesão está Errada!")


        if contador_acertos >= 6 and contador_segundario == 9:
            contador_aprovação+=1
            print(f"\n\nAluno com Matricula {matriculas[contador_primario]} está Aprovado com nota {contador_acertos} !!")
        elif contador_acertos < 6 and contador_segundario == 9:
            print(f"\n\nAluno com Matricula {matriculas[contador_primario]} está Reprovado com nota {contador_acertos} !!")

    input("\nAperte 'ENTER' para seguir: ")

porcentual_aprovacao = float((10 * contador_aprovação ) / 100) * 100

print(f"\nO porcentual de aprovação é de : {porcentual_aprovacao:.2f}%\n")
    
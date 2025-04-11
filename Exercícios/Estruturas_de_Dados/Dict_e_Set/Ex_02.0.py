#Codigo que contem dados e usa esses dados para calcular media e retornar a chave e valor da estrutura dict

questoes={'clara':[7,5,8],'bia':[3,7,5],'manu':[6,2,5],'tadeu':[1,2,3]}

for aluno, nota in questoes.items():
    boletin=sum(nota)/len(nota)
    print(f'\nAlun(a): {aluno}\nMedia: {boletin:.2f}\n\n')








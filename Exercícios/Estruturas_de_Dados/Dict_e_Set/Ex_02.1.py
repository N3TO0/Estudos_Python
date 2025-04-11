#Boletim com imput usando dict

print('{:-^80}'.format(' Calculo de Média '))
boletim={'Matematica':[0,0,0],'Português':[0,0,0],'Biologia':[0,0,0],'Ciencias':[0,0,0]}

print('\nColoque as notas das de cada materia\n')

for materia, notas in boletim.items():
   print(f'\n Materia: {materia}\n')
   while True:

      Novo_valor1=int(input('Primeira nota: ').strip())
      if Novo_valor1 > 10:
         print('Nota não existente!, faça novamente\n')
         continue
      Novo_valor2=int(input('Segunda nota: ').strip())
      if Novo_valor2 > 10:
         print('Nota não existente!, faça novamente\n')
         continue
      Novo_valor3=int(input('Terceira nota: ').strip())
      if Novo_valor3 > 10:
         print('Nota não existente!, faça novamente\n')
         continue
      
      boletim[materia]=[Novo_valor1,Novo_valor2,Novo_valor3] 
      break
print('{:-^80}'.format(' Resultado ')) 

print('\nAs médias de cada materia são:')
for materia, nota in boletim.items():
   media=sum(nota)/len(nota)
   print(f'\n{materia}\nMedia: {media:.2f}')
   
print('{:-^80}'.format(' Fim '))   
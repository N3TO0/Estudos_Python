# 1) Lista de Tarefas (To-Do List): Você está criando um aplicativo simples de
#    lista de tarefas. Um usuário precisa armazenar suas tarefas do dia. Ele deve ser
#    capaz de adicionar novas tarefas, marcar tarefas como concluídas (removê-las) e ver
#    as tarefas na ordem em que foram adicionadas.
 
# Resposta: Dict


# lista_de_tarefas={}
# contador=1

# while 1:

#     print('\n','-'*46)

#     resposta=int(input("\nEscolha as opções: \n\n1 - Adicionar item novo a lista\n2 - Marcar item como concluido da lista\n3 - Sair \n\nDigite: ").strip())

#     print('\n','-'*46)

#     if resposta == 1:
#         lista_de_tarefas[contador]=input("\nDigite o sua tarefa: ").strip()
        

#     elif resposta == 2:
#         indice_removedor=int(input("\nEscolha o numero do item que deseja remover: ").strip())

#         if indice_removedor in lista_de_tarefas:
#             lista_de_tarefas.pop(indice_removedor)
        
#         else:
#             print('\n','-'*46)
            
#             print("\nNão foi digitado nenhuma das opções! Por favor tente novamente !")
#             continue
        
#     elif resposta == 3:
#         break

#     else:
#         print("\nNão foi digitado nenhuma das opções! Por favor tente novamente !")
#         continue

#     print('\n','-'*15, "Lista de tarefas" , "-"*15 ,'\n')

#     for chave, valor in lista_de_tarefas.items():
#         print(f"{chave} - {valor}")


#     contador += 1


# --------------------------------------------------------------------------------------------------------------------


# 2) 

conjunto=set( 1, '1')

print(conjunto)
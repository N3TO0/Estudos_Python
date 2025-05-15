from datetime import datetime, timedelta

def calc_time(opcao):
    tempo_do_trabalho = data_atual + timedelta(minutes=opcao)
    return print(f"\nO carro chegou: {data_atual.strftime("%H:%M")} e estará pronto: {tempo_do_trabalho.strftime("%H:%M")}\n\n")

#Tempo que cliente solicitou
tempo_solicitado= str( input("""
Opção 1 ou P : Pacote Simples
                             
Opção 2 ou M : Pacote Médio
                                                        
Opção 3 ou G : Pacote Completo

                                                    
Desejo a opção: """))

#Tempo do trabalho em minutos.
TEMPO_PEQUENO = 30
TEMPO_MEDIO = 45
TEMPO_GRANDE = 60

data_atual= datetime.today() 

#Corpo de verificação e retorno.
if tempo_solicitado.lower() == "p" or tempo_solicitado.lower() == "pacote simples":
    calc_time(TEMPO_PEQUENO)

elif tempo_solicitado.lower() == "m" or tempo_solicitado.lower() == "pacote medio":
    calc_time(TEMPO_MEDIO)

elif tempo_solicitado.lower() == "g" or tempo_solicitado.lower() == "pacote completo":
    calc_time(TEMPO_GRANDE)

else:
    print("Opção não corresponde, tente novamente !!")
    

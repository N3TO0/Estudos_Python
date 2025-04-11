import pyautogui as pa
import time


#Primeiro ajeite os player na tela 1 e 2
#E deixe preenchido mas não maximizado total
#O resto é comigo :) 


#Alinhando linha do tempo inicial.
time.sleep(3)
pa.click(x=453, y=939)#Ajeitando na linha do tempo inicial tela 1
time.sleep(.5)
pa.click(x=85, y=941)#Ajeitando na linha do tempo inicial tela 1
time.sleep(2)
pa.click(x=-1358, y=539)#Ajeitando na linha do tempo inicial tela 2

#Sincronização
pa.click(x=958, y=997)#play tela 1
time.sleep(2.1)
pa.click(x=-1350, y=566)#Play tela 2


#Maximizando player 1
pa.click(x=1808, y=998)


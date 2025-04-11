import pyautogui as pa
import time


#Pular Para o Proximo ep 
time.sleep(1.5)
pa.click(x=1240, y=962) #Tela 1
time.sleep(1.5)
pa.click(x=-403, y=508) #Tela 2

#Pausar ep
time.sleep(2)
pa.click(x=-1294, y=331) #Tela 1
time.sleep(1.5)
pa.click(x=71, y=780) #Tela 2

#Pula a abertura
time.sleep(1)
pa.click(x=245, y=827) #Tela 1
pa.click(x=245, y=827) 
time.sleep(1)
pa.click(x=-1155, y=371) #Tela 2
pa.click(x=-1155, y=371)

#Maximiza 
time.sleep(1)
pa.click(x=-42, y=328) #Tela 1
time.sleep(1)
pa.click(x=1872, y=783) #Tela 2

# #Play geral
time.sleep(2)
pa.click(x=-1326, y=551)#play tela 1
pa.click(x=23, y=1014)#play tela 2

# # #Sincronização 
pa.click(x=-1326, y=551)#pause tela 1
time.sleep(1)# tempo de sincronização
pa.click(x=-1326, y=551)#play tela 1



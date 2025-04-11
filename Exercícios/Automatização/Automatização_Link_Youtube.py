import pyautogui as pa
import time

pa.PAUSE = 1  # Espera um segundo entre os comandos

pa.press("win")  # Pressiona a tecla Windows
pa.write("Opera GX")  # Digita "Opera GX"
pa.press("enter")  # Pressiona Enter para abrir o navegador

time.sleep(2)  # Espera o navegador carregar 

pa.hotkey("ctrl", "l")  # Ativa a barra de endereços
time.sleep(1)  # Pequena espera antes de digitar

pa.write("https://www.youtube.com")  # Digita devagar para evitar erros
pa.press("enter")  # Pressiona Enter para acessar o link

time.sleep(2)
pa.click(x=698, y=101)
pa.write("Falling Down - Lil Peep and XXXTentacion Cover")
pa.press("ENTER")

time.sleep(2)
pa.click(x=1147, y=495)


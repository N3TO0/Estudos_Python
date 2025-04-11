from selenium import webdriver
import time

#Abrir navegador
navegador=webdriver.Chrome()

#Abrir navegador no link
navegador.get("https://www.hashtagtreinamentos.com")


#Maximizar aba
navegador.maximize_window()

#Selecionar um elemento
botao1=navegador.find_element('class name','botao-verde')
botao1.click()

botao2=navegador.find_element('class name','header__titulo')

botao2.click()

botao3=navegador.find_elements('class name','header__lista-icone')

botao3[2].click()

#Selecionar aba
aba = navegador.window_handles
navegador.switch_to.window(aba[1])

#abre link na aba selecionada
navegador.get('https://www.youtube.com/watch?v=pZ6EqsHskM8')

#Seleciona o elemento e digita
botao=navegador.find_element('name','search_query')

#Seleciona o elemento e digita nele
botao.send_keys('Ei nerd')

#Dar scroll (colocar um elemento na tela)
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})",botao)

#Espera carregar para poder clicar
time.sleep(2)
botao.click()

# condição 2 para espera não ser direta
# from seleium.webdriver.support.ui import WebDriverWait
# from seleium.webdriver.support import expected_condition as EC
#   
# espera= WebDriverWait(navegador,10)
# espera.until(Ec.element_to_be_clickable(botao))
# 
# botao.click()
time.sleep(10000)
